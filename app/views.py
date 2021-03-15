from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View

from app.logic.calendar import create_calendar
from .forms import *
from .decorators import house_required


def index(request):
	return render(request, 'app/index.html')


@login_required  # This decorator needs to come first as @house_required depends on the user object to validate: it
# can't do that without a logged in user
@house_required
def dashboard(request):
	if request.method == 'GET':
		calendar = create_calendar()

		return render(request, 'app/dashboard.html', {'tasks': Task.objects.all(), 'calendar': calendar})

	else:
		calendar = create_calendar()
		tasks = {'tasks': Task.objects.all(),
				 'calendar': calendar}
		try:
			# title = models.CharField(max_length=50)
			# description = models.TextField()
			# date = models.DateField()
			# house = models.ForeignKey(House, on_delete=models.CASCADE)

			# author=request.user
			task_name = request.POST.get('task_name')
			task_description = request.POST.get('task_description')
			task_date_due = request.POST.get('task_date_due')

			# need to get author from
			new_calendar_entry = CalendarEntry(title=task_name, description=task_description, date=task_date_due,
											   house=request.house)
			new_calendar_entry.save()
			new_task = Task(author=request.user, date=new_calendar_entry)
			new_task.save()

		except:
			payment_name = request.POST.get('payment_name')
			payment_amount = request.POST.get('payment_amount')
			payment_date_due = request.POST.get('payment_date_due')
			payment_recipient = request.POST.get('recipient')
			payment_payees = request.POST.get('payees')

			# need to get author from
			new_calendar_entry = CalendarEntry(title=payment_name, description="", date=payment_date_due,
											   house=request.house)
			new_calendar_entry.save()
			new_payment = Expense(amount=payment_amount, recipient=payment_recipient, payees=payment_payees,
								  date=new_calendar_entry)
			new_payment.save()

		return render(request, 'app/index.html', tasks)


class SignUp(View):

	def get(self, request, userForm=None, profileForm=None):
		# If we haven't been passed a priorly created user form, create a new one
		if userForm is None:
			userForm = UserRegistrationForm()

			# Likewise for the profile form
			if profileForm is None:
				profileForm = ProfileRegistrationForm()

		return render(request, 'app/signup.html', {'userForm': userForm,
												   'profileForm': profileForm})

	def post(self, request):
		userForm = UserRegistrationForm(request.POST)
		profileForm = ProfileRegistrationForm(request.POST)

		if userForm.is_valid() and profileForm.is_valid():
			userForm.instance.Profile = profileForm.instance
			profileForm.instance.User = userForm.instance
			userForm.save()
			profileForm.save()
			return redirect("login")
		else:
			# We pass the userForm to the get request to allow it to populate it with the data that was there before then
			return self.get(request, userForm, profileForm)


def forgot_password(request):
	return render(request, 'app/password.html')


class Account(View):

	def get(self, request):
		userForm = UserUpdateForm(instance=request.user)
		profileForm = ProfileUpdateFrom(instance=request.user.Profile)

		context = {'userForm': userForm,
				   'profileForm': profileForm}

		return render(request, 'app/account.html', context)

	def post(self, request):
		userForm = UserUpdateForm(request.POST, instance=request.user)
		profileForm = ProfileUpdateFrom(request.POST, instance=request.user.Profile)

		if userForm.is_valid() and profileForm.is_valid():
			userForm.save()
			profileForm.save()

		return self.get(request)


class CreateHouse(View):
	def get(self, request):
		return render(request, 'app/create-house.html')

	def post(self, request):
		houseName = request.POST.get('house-name')
		house = House(name=houseName)
		house.save()

		membership = HouseMembership(house=house, user=request.user, currentHouse=True, admin=True)
		membership.save()

		return redirect('dashboard')


class JoinHouse(View):

	def get(self, request):
		return render(request, 'app/join-house.html')

	def post(self, request):
		houseCode = request.POST.get('code')
		house = House.objects.get(uniqueCode=houseCode)

		membership = HouseMembership(house=house, user=request.user, currentHouse=True, admin=False)
		membership.save()

		return redirect('dashboard')


class HousePage(View):
	def get(self, request, form=None):
		house = request.user.house_set.first()  # If we ever allow multiple people to have houses then we'll have to
		# change this to use a foreign key

		rooms = house.room.all()

		if form is None:
			form = HouseUpdateForm(instance=house)

		context = {'form': form,
				   'house': house,
				   'rooms': rooms}

		return render(request, 'app/house.html', context)

	def post(self, request):
		house = request.user.house_set.get(housemembership__currentHouse=True)

		if 'codeGenerator' in request.POST:
			house.generateNewCode()
			return self.get(request)

		form = HouseUpdateForm(request.POST, instance=house)

		if form.is_valid():
			form.save()

		return self.get(request, form)


check = False


class AddRoom(View):

	def get(self, request):  # , form=None
		house = request.user.house_set.get(housemembership__currentHouse=True)
		rooms = house.room.all()

		if check is True:
			return redirect('rent-distribution')

		'''if form is None:
			form = AddRoomForm()
		else:
			return redirect('rent-distribution')'''
		# 'form': form,

		context = {'house': house, 'rooms': rooms}

		return render(request, 'app/add-room.html', context)

	def post(self, request):
		house = request.user.house_set.get(housemembership__currentHouse=True)
		room_name = request.POST.get('room-name')
		rent_amount = request.POST.get('rent-amount')
		room = Room(name=room_name, rent=rent_amount, house=house)
		room.save()
		check = True

		return redirect('rent-distribution')


class RentDistribution(View):

	def get(self, request, form=None):
		house = request.user.house_set.get(housemembership__currentHouse=True)
		rooms = house.room.all()
		if form is None:
			form = RoomUpdateForm()

		context = {'form': form, 'house': house, 'rooms': rooms}

		return render(request, 'app/rent-distribution.html', context)

	def post(self, request):
		# house = request.user.house_set.get(housemembership__currentHouse=True)
		# room = house.room.name()
		# form = RoomUpdateForm(request.POST, instance=)

		# if form.is_valid():
			# form.instance.
		# house = request.user.house_set.get(housemembership__currentHouse=True)
		# room_name = request.POST.get('room-name')
		# rent_amount = request.POST.get('rent-amount')
		# room = Room(name=room_name, rent=rent_amount, house=house)
		# room.save()

		return self.get(request)

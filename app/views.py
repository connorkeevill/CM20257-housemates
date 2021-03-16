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
	# If we are processing a POST request here
	if request.method == 'POST':
		try:
			task_name = request.POST.get('task_name')
			task_description = request.POST.get('task_description')
			task_date_due = request.POST.get('task_date_due')

			# need to get author from
			new_calendar_entry = CalendarEntry(title=task_name, description=task_description, date=task_date_due,
											   house=request.user.house_set.first())
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
											   house=request.user.house_set.first())
			new_calendar_entry.save()
			new_payment = Expense(amount=payment_amount, recipient=payment_recipient, payees=payment_payees,
								  date=new_calendar_entry)
			new_payment.save()

	calendar = create_calendar()
	house = request.user.house_set.first()
	payments = Expense.objects.filter(date__house=house)
	tasks = Task.objects.filter(date__house=house)

	return render(request, 'app/dashboard.html', {'tasks': tasks, 'calendar': calendar, 'house': house, 'payments': payments})


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

		house = request.user.house_set.first()

		context = {'userForm': userForm,
				   'profileForm': profileForm,
				   'house': house}

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

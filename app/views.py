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
            task_name = request.POST.get('task_name')
            task_description = request.POST.get('task_description')
            task_date_due = request.POST.get('task_date_due')

            # need to get author from
            new_task = Task(title=task_name, description=task_description, date_due=task_date_due, author=request.user)
            new_task.save()

        except:
            payment_name = request.POST.get('payment_name')
            payment_amount = request.POST.get('payment_amount')
            payment_date_due = request.POST.get('payment_date_due')

            # need to get author from
            new_payment = Payment(title=payment_name, amount=payment_amount, date_due=payment_date_due,
                                  author=request.user)
            new_payment.save()

        return render(request, 'app/index.html', tasks)


class SignUp(View):

    def get(self, request, userForm=None, profileForm=None):
        # If we haven't been passed a priorly created user form, create a new one
        if userForm is None:
            userForm = UserRegistrationForm()

        # Likewise for the profile form
        if profileForm is None:
            profileForm = ProfileForm()

        return render(request, 'app/signup.html', {'userForm': userForm,
                                                   'profileForm': profileForm})

    def post(self, request):
        userForm = UserRegistrationForm(request.POST)
        profileForm = ProfileForm(request.POST)

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
        profileForm = ProfileForm(instance=request.user.Profile)

        context = {'userForm': userForm,
                   'profileForm': profileForm}

        return render(request, 'app/account.html', context)

    def post(self, request):
        userForm = UserUpdateForm(request.POST, instance=request.user)
        profileForm = ProfileForm(request.POST, instance=request.user.Profile)

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
        house.inhabitants.add(request.user)

        return redirect('dashboard')


class JoinHouse(View):

    def get(self, request):
        return render(request, 'app/join-house.html')

    def post(self, request):
        houseCode = request.POST.get('code')
        house = House.objects.get(uniqueCode=houseCode)

        house.inhabitants.add(request.user)

        return redirect('dashboard')

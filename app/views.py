from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.shortcuts import render, redirect
from django.views import View

from app.logic.calendar import create_calendar
from app.models import Task


def dashboard(request):
	calendar = create_calendar()
	tasks = {'tasks': Task.objects.all(),
			 'calendar': calendar}
	# payments = {'payments': Payment.object.all()}
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

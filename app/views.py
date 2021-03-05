from django.shortcuts import render, redirect
from django.views import View

from app.logic.calendar import create_calendar
from app.models import Task
from .forms import *


def dashboard(request):

	calendar = create_calendar()
	tasks = Task.objects.all()
	tasks = []

	if request.method == 'GET':

		# payments = {'payments': Payment.object.all()}
		return render(request, 'app/index.html', {'tasks': tasks, 'calendar': calendar})
	else:
		tasks = {'tasks': tasks,
				 'calendar': calendar}

		task_name = request.POST.get('task_name')
		task_description = request.POST.get('task_description')
		task_date_due = request.POST.get('task_date_due')

		# need to get author from
		new_task = Task(title=task_name, description=task_description, date_due=task_date_due, author=request.user)
		new_task.save()

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



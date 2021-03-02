from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *


class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class ProfileRegistrationForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['firstName', 'surname', 'DOB']

class TaskCreatorForm(forms.Form):
	class Meta:
		fields = ['']
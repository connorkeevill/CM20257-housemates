from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import *


class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class ProfileUpdateFrom(ModelForm):
	class Meta:
		model = Profile
		fields = ['firstName', 'surname', 'DOB', 'status']

class ProfileRegistrationForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['firstName', 'surname', 'DOB']


class UserUpdateForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email']


class HouseUpdateForm(ModelForm):
	class Meta:
		model = House
		fields = ['name', 'inhabitants']

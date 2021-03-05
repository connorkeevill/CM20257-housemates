from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *


class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['firstName', 'surname', 'DOB']


class UserUpdateForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email']


class JoinHouseForm(ModelForm):
	class Meta:
		model = JoinHouse
		fields = ['code']

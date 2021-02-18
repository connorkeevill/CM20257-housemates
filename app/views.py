from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


def login(request):
	return render(request, 'app/login.html')


def dashboard(request):
	return render(request, 'app/index.html')


class SignUp(View):

	def get(self, request, form=None):
		if form is None:
			form = UserCreationForm()
		return render(request, 'app/signup.html', {'form': form})

	def post(self, request):
		form = UserCreationForm(request.POST)
		if form.is_valid():
			return HttpResponse("I'm happy")
		else:
			return self.get(request, form)


def forgot_password(request):
	return render(request, 'app/password.html')

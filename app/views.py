from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class Login(View):

	def get(self, request):
		return render(request, 'app/login.html')

	def post(self, request):
		pass


def dashboard(request):
	return render(request, 'app/index.html')


class SignUp(View):

	def get(self, request, form=None):
		# If we haven't been passed a priorly created form, create a new one
		if form is None:
			form = UserCreationForm()

		return render(request, 'app/signup.html', {'form': form})

	def post(self, request):
		form = UserCreationForm(request.POST)

		if form.is_valid():
			return HttpResponse("I'm happy")
		else:
			# We pass the form to the get request to allow it to populate it with the data that was there before then
			return self.get(request, form)


def forgot_password(request):
	return render(request, 'app/password.html')

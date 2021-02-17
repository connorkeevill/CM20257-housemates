from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return render(request, 'app/login.html')


def dashboard(request):
    return render(request, 'app/index.html')


def signup(request):
    return render(request, 'app/signup.html')


def forgot_password(request):
    return render(request, 'app/password.html')
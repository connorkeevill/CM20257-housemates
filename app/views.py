from django.shortcuts import render
from .models import Task
from django.http import HttpResponse


def login(request):
    return render(request, 'app/login.html')


def dashboard(request):
    tasks = {'tasks': Task.objects.all()}
    return render(request, 'app/index.html', tasks)


def signup(request):
    return render(request, 'app/signup.html')


def forgot_password(request):
    return render(request, 'app/password.html')

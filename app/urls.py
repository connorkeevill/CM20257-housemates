from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),
]
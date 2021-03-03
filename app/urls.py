from django.urls import path
from django.contrib.auth import views as authenticationViews
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('login/', authenticationViews.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),
    path('logout/', authenticationViews.LogoutView.as_view(template_name='app/logout.html'), name='logout'),
    path('account/', login_required(views.Account.as_view()))
]
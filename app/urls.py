from django.contrib.auth import views as authenticationViews
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('login/', authenticationViews.LoginView.as_view(template_name='app/login.html'), name='login'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('signup/', views.SignUp.as_view(), name='signup'),
	path('forgot-password/', views.forgot_password, name='forgot-password'),
	path('logout/', authenticationViews.LogoutView.as_view(template_name='app/logout.html'), name='logout'),
	path('account/', login_required(views.Account.as_view()), name='account'),
	path('join-house/', login_required(views.JoinHouse.as_view()), name='join-house'),
	path('create-house/', login_required(views.CreateHouse.as_view()), name='create-house'),
	path('house/', house_admin_required(login_required(views.HousePage.as_view())), name='house'),
	path('shopping-list/', login_required(house_required(views.ShoppingList.as_view())), name='shopping-list'),
	path('shopping-list-complete/<int:id>/', views.completeShoppingList, name='shopping-list-complete'),
	path('calendar-item-complete/<int:id>/', views.completeCalendarItem, name='calendar-item-complete'),
	path('rent-distribution/', views.RentDistribution.as_view(), name='rent-distribution')
]

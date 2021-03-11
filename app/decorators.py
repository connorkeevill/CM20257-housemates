from django.shortcuts import redirect
from .models import HouseMembership


def house_required(function=None):
	def wrapper(request, *args, **kwargs):
		user = request.user

		try:
			currentHouse = HouseMembership.objects.get(user=user, currentHouse=True)
		except HouseMembership.DoesNotExist:
			currentHouse = None

		if currentHouse is not None:
			return function(request)

		return redirect('join-house')

	return wrapper


def house_admin_required(function=None):
	def wrapper(request, *args, **kwargs):
		user = request.user

		# Get the user's current house, only if they are an admin
		try:
			membership = HouseMembership.objects.get(user=user, currentHouse=True, admin=True)
		except HouseMembership.DoesNotExist:
			membership = None

		if membership is not None:
			return function(request)

		return redirect('dashboard')

	return wrapper

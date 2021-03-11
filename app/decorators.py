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

from django.shortcuts import redirect


def house_required(function=None):
	def wrapper(request, *args, **kwargs):
		user = request.user
		if len(user.house_set.all()) > 0:
			return function(request)

		return redirect('join-house')
	return wrapper

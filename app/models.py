from django.contrib.auth.models import User, Group
from django.db import models
import random, string


# Create your models here.
class Task(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	date_due = models.DateTimeField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title


class Status(models.Model):
	type = models.CharField(max_length=20)
	description = models.TextField()

	def __str__(self):
		return self.type


# Profiles are used with a one-to-one relationship with users to allow more data to be stored, that django doesn't
# handle.
class Profile(models.Model):
	User = models.OneToOneField(User, models.CASCADE, related_name='Profile')
	firstName = models.CharField(max_length=26)
	surname = models.CharField(max_length=26)
	DOB = models.DateField()
	status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.firstName + " " + self.surname + ": " + self.User.username


# class JoinHouse(models.Model):
# 	house_name = 'My House'
# 	house_members = models.ManyToManyField(User, related_name='house_members')
# 	join_code = models.CharField(max_length=10)
# 	house = Group.objects.get(name=house_name, join_code=request.POST.get('join_code'))
# 	house.house_members.add(request.user)

class House(models.Model):
	name = models.CharField(max_length=20)
	uniqueCode = models.CharField(max_length=10)
	inhabitants = models.ManyToManyField(User)

	# Creates the code for the house
	def createUniqueCode(self):
		allChars = string.ascii_letters + string.digits
		code = ""

		for i in range(10):
			code += random.choice(allChars)

		self.uniqueCode = code



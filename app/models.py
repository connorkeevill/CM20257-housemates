import random
import string

from django.contrib.auth.models import User, Group
from django.db import models


# Create your models here.


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


class Status(models.Model):
	type = models.CharField(max_length=20)
	description = models.TextField()

	def __str__(self):
		return self.type


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

	# Overrides parent method to enforce the creation of a unique code upon saving
	def save(self, force_insert=False, force_update=False, using=None,
			 update_fields=None):

		if self.uniqueCode == "":
			self.createUniqueCode()
		super().save(force_insert, force_update, using, update_fields)


class Task(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	date_due = models.DateTimeField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	hosue = models.ForeignKey(House, on_delete=models.CASCADE())

	def __str__(self):
		return self.title

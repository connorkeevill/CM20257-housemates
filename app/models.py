import random
import string
from django.contrib.auth.models import User, Group
from django.db import models


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
	status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.firstName + " " + self.surname + ": " + self.User.username


class House(models.Model):
	name = models.CharField(max_length=20)
	uniqueCode = models.CharField(max_length=10)
	inhabitants = models.ManyToManyField(User, through='HouseMembership')

	# Creates the code for the house
	def createUniqueCode(self):
		allChars = string.ascii_letters + string.digits
		code = ""

		for i in range(10):
			code += random.choice(allChars)

		self.uniqueCode = code

	def generateNewCode(self):
		self.createUniqueCode()
		self.save()

	# Overrides parent method to enforce the creation of a unique code upon saving
	def save(self, force_insert=False, force_update=False, using=None,
			 update_fields=None):

		if self.uniqueCode == "":
			self.createUniqueCode()
		super().save(force_insert, force_update, using, update_fields)

	def __str__(self):
		return self.name


class HouseMembership(models.Model):
	house = models.ForeignKey(House, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	admin = models.BooleanField(default=False)
	currentHouse = models.BooleanField(default=False)


class CalendarEntry(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()
	date = models.DateField()
	house = models.ForeignKey(House, on_delete=models.CASCADE)

	def __str__(self):
		return self.title


class Task(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.OneToOneField(CalendarEntry, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.date.title

	def year_month_day(self):
		return self.date.strftime('%Y,%m-1,%d')


class Expense(models.Model):
	amount = models.IntegerField()  # We should store these amounts in pence, not pounds - otherwise we may get floating
	# point problems
	recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incomingPayment')
	payees = models.ManyToManyField(User)
	date = models.OneToOneField(CalendarEntry, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.date.title


class Room(models.Model):
	name = models.CharField(max_length=20)
	inhabitant = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='room', null=True)
	house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='room')
	rent = models.IntegerField()  # Again, it's a good idea to store the rent in pence


class ShoppingItem(models.Model):
	name = models.CharField(max_length=30)
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	house = models.ForeignKey(House, on_delete=models.CASCADE)
	complete = models.BooleanField(default=False)

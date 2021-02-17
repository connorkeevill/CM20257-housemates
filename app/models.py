from django.db import models


class User(models.Model):
	first_name = models.CharField(max_length=30)
	surname = models.CharField(max_length=30)
	date_of_birth = models.DateField()

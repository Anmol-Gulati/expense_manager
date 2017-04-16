import datetime

from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
	category = models.CharField(max_length=255)

	def __str__(self):
		return self.category


class Amount(models.Model):
	description = models.TextField()
	amount = models.IntegerField(default=0)
	user = models.ForeignKey(User)
	created_at = models.DateField(("Date"), auto_now_add=True)
	category = models.ForeignKey(Expense)

	def __str__(self):
		return self.description[:10]		
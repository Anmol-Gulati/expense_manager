from django.db import models

from django.contrib.auth.models import User


class Expense(models.Model):
	category = models.CharField(max_length=255)
	description = models.TextField()
	amount = models.IntegerField(default=0)
	user = models.ForeignKey(User)

	def __str__(self):
		return self.category
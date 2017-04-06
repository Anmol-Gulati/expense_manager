from rest_framework import serializers

from . import models


class ExpenseSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'category',
			'amount'
		)
		model = models.Expense
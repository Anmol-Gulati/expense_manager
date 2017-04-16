from rest_framework import serializers

from . import models


class AmountSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'category',
			'amount',
			'description',
			'created_at'
		)
		model = models.Amount
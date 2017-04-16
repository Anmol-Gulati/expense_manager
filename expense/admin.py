from django.contrib import admin

from . import models


class AmountAdmin(admin.ModelAdmin):
	list_display = ['category', 'user', 'amount', 'created_at']

admin.site.register(models.Expense)
admin.site.register(models.Amount, AmountAdmin)
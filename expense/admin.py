from django.contrib import admin

from . import models


class ExpenseAdmin(admin.ModelAdmin):
	list_display = ['category', 'user', 'amount']

admin.site.register(models.Expense, ExpenseAdmin)
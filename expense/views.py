from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from . import models

@login_required
def add_expense(request):
	if request.method == 'POST':
		category = request.POST.get('category')
		description = request.POST.get('description')
		amount = request.POST.get('amount')

		models.Expense.objects.create(
			category=category,
			description=description,
			amount=amount,
			user=request.user
		)

		success_message = "Expense Successfully Added."

		return render(request, 'expense/expense_form.html', {'success_message': success_message})

	return render(request, 'expense/expense_form.html')
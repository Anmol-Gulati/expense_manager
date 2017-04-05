from django.shortcuts import render


def add_expense(request):
	return render(request, 'expense/expense_form.html')
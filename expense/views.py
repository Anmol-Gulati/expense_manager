from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers


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



def view_expense(request):
	return render(request, 'expense/view_expense.html')


class ListExpense(APIView):

    def get(self, request, format=None):
        expenses = models.Expense.objects.filter(user=self.request.user)
        serializer = serializers.ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ListExpense, self).dispatch(*args, **kwargs)    		
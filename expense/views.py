
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import JsonResponse

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

		expense, created = models.Expense.objects.get_or_create(category=category)

		if expense:
			models.Amount.objects.create(
				category=expense,
				description=description,
				amount=amount,
				user=request.user
			)
		else:
			models.Amount.objects.create(
				category=created,
				description=description,
				amount=amount,
				user=request.user
			)				

		success_message = "Expense Successfully Added."

		return render(request, 'expense/expense_form.html', {'success_message': success_message})

	return render(request, 'expense/expense_form.html')	


@login_required
def view_expense(request):
	return render(request, 'expense/view_expense.html')


class ListAmount(APIView):

    def get(self, request, format=None):
        amounts = models.Amount.objects.filter(user=self.request.user)
        serializer = serializers.AmountSerializer(amounts, many=True)
        return Response(serializer.data)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ListAmount, self).dispatch(*args, **kwargs)


@login_required
def view_pie_expense(request):
	expenses = models.Expense.objects.all()
	amount_list = []
	expense_on_list = []

	for expense in expenses:
		amounts = models.Amount.objects.filter(category=expense, user=request.user)
		print(amounts)

		total_amount = 0


		for amount in amounts:
			total_amount += amount.amount

		expense_on_list.append(expense.category)
		amount_list.append(total_amount)


	return JsonResponse({'expense': expense_on_list,
						 'amount': amount_list})


@login_required
def view_bar_expense(request):
	created_at_list = []
	amount_list = []

	amounts = models.Amount.objects.filter(user=request.user)

	for amount in amounts:
		print(amount.created_at)
		created_at_list.append(amount.created_at)

	created_at_list = list(set(created_at_list))

	for date in created_at_list:
		amounts = models.Amount.objects.filter(user=request.user, created_at=date)

		total_amount = 0


		for amount in amounts:
			total_amount += amount.amount

		amount_list.append(total_amount)		

	return JsonResponse({'created_at': created_at_list,
						 'amount': amount_list})						 		 
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'add/', views.add_expense, name='add_expense'),
	url(r'view_expense/', views.view_expense, name='view_expense'),
	url(r'^$', views.ListExpense.as_view(), name='expense_list'),	
]
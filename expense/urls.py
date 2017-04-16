from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'add/', views.add_expense, name='add_expense'),
	url(r'view_expense/', views.view_expense, name='view_expense'),
	url(r'view_pie_expense/', views.view_pie_expense, name='view_pie_expense'),
	url(r'view_bar_expense/', views.view_bar_expense, name='view_bar_expense'),
	url(r'^$', views.ListAmount.as_view(), name='expense_list'),	
]
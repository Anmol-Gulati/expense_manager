from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'add/', views.add_expense, name='add_expense'),	
]
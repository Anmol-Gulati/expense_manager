from django.shortcuts import render
from django.http import HttpResponseRedirect


def welcome_view(request):
	return render(request, 'welcome.html')

def home_view(request):
	return render(request, 'home.html')	
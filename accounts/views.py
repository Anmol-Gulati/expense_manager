from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def register(request):

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/login')

	form = UserCreationForm()
	return render(request, 'accounts/registration_form.html', {'form': form})


def login_view(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/expense/view_expense')
		error = "Invalid Credentials"
		return render(request, 'accounts/login.html', {'error': error})			

	return render(request, 'accounts/login.html')
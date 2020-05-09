from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def register(response):
	if response.user.is_authenticated:
		return render(response, "list_form.html", {})
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(response, user)
			return render(response, "list_form.html", {})
	else:
		form = RegisterForm()
	return render(response, "signup.html", {"form":form})

@login_required
def logout_view(request):
	logout(request)
	return render(request, "login.html", {})

def login_view(request):
	if request.user.is_authenticated:
		return render(request, "list_form.html", {})
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return render(request, "list_form.html", {})
			else:
				return HttpResponse("Your account is disabled.")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request, "login.html", {})

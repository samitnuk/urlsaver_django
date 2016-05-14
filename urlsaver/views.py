from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from django.http import HttpResponse

from .forms import (LoginForm, RegistrationForm,
                    EditForm, SearchForm, RestorePasswordForm)

def main_view(request):
    return render(request, 'main.html')


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # as username will be used part of email before '@'
            username = email.split('@')[0]
            password = form.cleaned_data['password']
            user = User(username=username, password=password, email=email)
            user.save()
            return redirect('main') # name for main_view in urls
    else: # if a GET (or any other method) we'll create a blank form
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def logout_view(request):
    return HttpResponse("Logout View")

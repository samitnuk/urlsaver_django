from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse


def main_view(request):
    return HttpResponse("Hello, World! This is main page!")


def register_view(reguest):
    return HttpResponse("Register View")


def login_view(reguest):
    return HttpResponse("Login View")


@login_required
def logout_view(reguest):
    return HttpResponse("Logout View")

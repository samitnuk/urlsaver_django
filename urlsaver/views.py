from django.shortcuts import render

from django.http import HttpResponse

def main_view(request):
    return HttpResponse("Hello, World! This is main page!")

def register_view(reguest):
    return HttpResponse("Register View")

def login_view(reguest):
    return HttpResponse("Login View")

def logout_view(reguest):
    return HttpResponse("Logout View")

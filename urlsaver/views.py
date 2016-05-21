from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_user
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from django.http import HttpResponse

from .forms import (LoginForm, RegistrationForm,
                    EditForm, SearchForm, RestorePasswordForm)

from .models import Locator
from .helpers import add_scheme, url_exists, get_title

# INNER HELPERS |------------------------------------------------------------

def get_urls(username):
    return Locator.objects.filter(username__username=username) \
                          .order_by('-date')

def get_groupnames(username):
    return list(set(Locator.objects \
                  .filter(username__username=username) \
                  .values_list('groupname', flat=True)))

def save_url(request, username, path, groupname):
    locator = Locator(url=add_scheme(path), title=get_title(path),
                      groupname=groupname, username=username)
    locator.save()
    if request.session.get('url', False):
        request.session['url'] = ''
        request.session['groupname'] = ''
    return redirect(request, 'main')


# VIEWS |--------------------------------------------------------------------

def main(request):
    if request.user.is_authenticated:
        # if request.session.get('url', False):
        #     save_url(request,
        #              request.user.username,
        #              request.session['url'],
        #              request.session['groupname'])
        if request.method == "POST":
            form = SearchForm(request.POST)
            if form.is_valid():
                query = form.cleaned_data['search']
                return redirect(request, 'search_results', {'query': query})
        else:
            context ={}
            context['form'] = SearchForm()
            context['urls'] = get_urls(request.user.username)
            context['groupnames'] = get_groupnames(request.user.username)
            print(context['groupnames'])
            return render(request, 'urls.jade', context)

    return render(request, 'home.jade')

def main_with_path(request, path):
    path = get_groupnames(request.user.username)
    return render(request, 'main_test.jade', {'path': path})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # as username will be used part of email before '@'
            username = email.split('@')[0]
            password = form.cleaned_data['password']
            user = User.objects.create_user(username, email, password)
            return redirect('login')
    else: # if a GET (or any other method) we'll create a blank form
        form = RegistrationForm()

    return render(request, 'register.jade', {'form': form})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # as username will be used part of email before '@'
            username = email.split('@')[0]
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login_user(request, user)
                return redirect('main')
    else: # if a GET (or any other method) we'll create a blank form
        form = LoginForm()
    return render(request, 'login.jade', {'form': form})


@login_required(login_url='/login/')
def logout(request):
    logout(request)
    return render(request, 'main.html')

def restore_password(request):
    pass

@login_required(login_url='/login/')
def groupname(request, groupname):
    pass

@login_required(login_url='/login/')
def edit(request, id):
    pass

@login_required(login_url='/login/')
def delete(request, id):
    pass

@login_required(login_url='/login/')
def search_results(request, query):
    pass


def contact(request):
    return render(request, 'contact.jade')


def about(request):
    return render(request, 'about.jade')

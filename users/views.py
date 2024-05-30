from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect(to="home:home")
        else:
            messages.error(request, 'Please correct the error below.')

    else:
        form = UserCreationForm()

    return render(request, template_name='users/signup.html', context={'form': form, "title": "Sign Up"})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user=user)
                return redirect(to='users:signup')
            else:
                messages.error(request, f"{username} isn't a valid one")
        else:
            messages.error(request, 'Please correct the error below.')
    elif request.method == "GET":
        form = UserLoginForm()
        return render(request, template_name='users/login.html', context={'form': form, "title": "Login"})


def logout_view(request):
    pass

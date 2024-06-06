from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def signup_view(request):
    if request.method == 'POST':
        # print("--" * 100)
        # print(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('users:login')
        else:
            for field, errors in form.errors.items():
                messages.error(request, f"{field}: {errors}")

    elif request.method == "GET":
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})
    else:
        print("-" * 100)
        print("OTHERS COMES")


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'welcome {username}')
                return redirect('home:home')
            else:
                messages.error(request, message=f"WE Didn't found your account")
                return redirect('users:signup')
        else:
            return HttpResponse(str(form.errors))
    else:
        form = UserLoginForm()
        return render(request, 'users/login.html', {'form': form})


@login_required
def logout_view(request):
    if request.user.is_anonymous:
        messages.success(request, 'You are not logged in')
        return redirect('home:home')
    else:
        logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('home:home')

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
                login(request, user)
                return redirect('home:home')  # Adjust the redirect URL as needed
            else:
                form.add_error(None, "Invalid username or password.")
                return redirect('users:signup')
        else:
            messages.error(request, 'Please correct the error below.')  # Form-level error for invalid form
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form, 'title': 'Login'})


def logout_view(request):
    try:
        # Log out the user
        logout(request)

        # Add a success message
        messages.success(request, 'You have been successfully logged out.')
    except Exception as e:
        # Handle any unexpected errors during logout
        messages.error(request, f'An error occurred: {str(e)}')

    # Redirect the user to the home page
    return redirect('home:home')

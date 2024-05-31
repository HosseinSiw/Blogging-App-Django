from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = get_user_model()

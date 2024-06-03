from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=50, min_length=10, required=True)
    phone_number = forms.CharField(max_length=11, min_length=11, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1')


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                raise forms.ValidationError("Invalid username.")
            else:
                user.check_password(password)
                if not user.is_active:
                    raise forms.ValidationError("User account is disabled.")
        else:
            raise forms.ValidationError("Both fields are required.")

from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    # path("logout/<int:id>/", views.logout_view, name="logout"),
]

from django.shortcuts import render
from django.contrib import messages


def home_view(request):
    context = {}
    if request.user.is_authenticated:
        context["msg"] = messages.success(request, message=f'WELCOME BACK {request.user.username}')
    return render(request, template_name="home/index-1.html", context=context)

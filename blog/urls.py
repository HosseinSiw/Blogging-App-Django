from django.urls import path
from blog import views


urlpatterns = [
    path('blogs', views.blog_list, name='blog-home'),
]

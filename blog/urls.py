from django.urls import path
from blog import views


app_name = 'blog'
urlpatterns = [
    path('blogs', views.blog_list, name='blog-home'),
    path("blogs/<int:pk>", views.blog_details, name="blog-details"),
]

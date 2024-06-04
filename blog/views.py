from django.shortcuts import render
from .models import Blog


def blog_list(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, template_name='blog/blog.html', context=context)


def blog_details(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {'blog': blog}
    return render(request, template_name='blog/detail.html', context=context)

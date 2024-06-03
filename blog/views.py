# from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Blog

blog_details_template = 'blog_details.html'  # UPDATE IT


def blog_list(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, template_name='Blog/blog_list.html', context=context)


# @login_required
def blog_details(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    context = {'blog': blog}
    return render(request, template_name=blog_details_template, context=context)

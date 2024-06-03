from django.shortcuts import render
from .models import Blog


# Create your views here.
def blog_list(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, template_name='Blog/blog_list.html', context=context)

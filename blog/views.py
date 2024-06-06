from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Blog, Comment
from .forms import CommentForm
from django.http import HttpResponseForbidden


def blog_list(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, template_name='blog/blog.html', context=context)


def blog_details(request, pk):
    comment_form = CommentForm()
    comments = Comment.objects.filter(blog_id=pk)
    blog = Blog.objects.get(pk=pk)
    context = {'blog': blog, "comments": comments, "comment_form": comment_form}

    if request.method == "GET":
        return render(request, template_name='blog/detail.html', context=context)

    elif request.method == "POST":
        if request.user.is_anonymous:  # Login Required for commenting
            return HttpResponseForbidden
        else:
            form = CommentForm(request.POST)
            if form.is_valid():
                content = request.POST.get('content')
                comment = Comment.objects.create(title=content, author=request.user, blog=blog)
                comment.save()
                messages.success(request, 'Your comment has been posted')
                return redirect(blog.get_absolute_url())

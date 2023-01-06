from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from .models import User, Post


def users(request: HttpRequest):
    users = User.objects.all()
    context = {
        "users": users,
    }
    return render(request, 'blog/users.html', context=context)


def posts(request: HttpRequest):
    posts = Post.objects.select_related("user").all()
    context = {
        "posts": posts,
    }
    return render(request, 'blog/posts.html', context=context)


def post_details(request: HttpRequest, pk: int):
    post = get_object_or_404(
        Post.objects.select_related("user"),
        pk=pk,
    )

    context = {
        "post": post,
    }
    return render(request, "blog/post_details.html", context=context)


def user_details(request: HttpRequest, pk: int):
    user = get_object_or_404(
        User.objects,
        pk=pk,
    )
    user_posts = Post.objects.filter(user=user)

    context = {
        "user": user,
        "user_posts": user_posts,
    }
    return render(request, "blog/user_details.html", context=context)

from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post, BlogUser, post


def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(request, 'blog/index.html', context)

def detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post':post,
    }
    return render(request, 'blog/detail.html', context)

def like_detail(request, pk):
    post = Post.objects.get(id=pk)
    post_likes= post.postlike_set.all()
    context = {
        'post_likes':post_likes,
    }
    return render(request, 'blog/like_detail.html', context)

def user_detail(request, pk):
    post = Post.objects.get(id=pk)
    user = BlogUser.objects.get(id=post.user_id)
    posts = user.post_set.all()
    context = {
        'posts':posts,
    }
    return render(request, 'blog/user_detail.html', context)




def create(request):
    return render(request, 'blog/create.html')

from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post


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
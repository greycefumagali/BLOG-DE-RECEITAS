from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html',
                  {'posts': posts})


def doces(request):
    posts = Post.objects.filter(categoria='1')
    return render(request, 'index.html',
                  {'posts': posts})


def salgadas(request):
    posts = Post.objects.filter(categoria='2')
    return render(request, 'index.html',
                  {'posts': posts})


def festas(request):
    posts = Post.objects.filter(categoria='3')
    return render(request, 'index.html',
                  {'posts': posts})


def cafe_lanches(request):
    posts = Post.objects.filter(categoria='4')
    return render(request, 'index.html',
                  {'posts': posts})


def exibir_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'exibir_post.html',
                  {'post': post})


def exibir_autor(request, autor_id):
    posts = Post.objects.filter(autor=autor_id)
    return render(request, 'index.html',
                  {'posts': posts})
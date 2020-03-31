from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Blog


# Create your views here.
def home(request):
    return render(request, 'blog/home.html')


def all_blogs(request):
    blogs = Blog.objects.all().order_by('-publish')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})


def cat_one(request):
    blogs = Blog.objects.filter(category='Category 1').order_by('-publish')
    return render(request, 'blog/category_one.html', {'blogs': blogs})


def cat_two(request):
    blogs = Blog.objects.filter(category='Category 2').order_by('-publish')
    return render(request, 'blog/category_two.html', {'blogs': blogs})


def cat_three(request):
    blogs = Blog.objects.filter(category='Category 3').order_by('-publish')
    return render(request, 'blog/category_three.html', {'blogs': blogs})

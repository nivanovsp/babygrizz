from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Blog
from .models import Filter


# Create your views here.
def home(request):
    return render(request, 'blog/home.html')


def blog(request):
    blogs = Blog.objects.all()
    f = Filter(request.GET, queryset=Blog.objects.order_by('-publish')[:6])
    return render(request, 'blog/blog.html', {'blogs': blogs, 'filter': f})


def all_blogs(request):
    blogs = Blog.objects.all()
    f = Filter(request.GET, queryset=Blog.objects.all().order_by('-publish'))
    return render(request, 'blog/all_blogs.html', {'blogs': blogs, 'filter': f})


def cat_one(request):
    blogs = Blog.objects.all()
    f = Filter(request.GET, queryset=Blog.objects.all().order_by('-publish'))
    return render(request, 'blog/category1.html', {'blogs': blogs, 'filter': f})


def cat_two(request):
    blogs = Blog.objects.all()
    f = Filter(request.GET, queryset=Blog.objects.all().order_by('-publish'))
    return render(request, 'blog/category2.html', {'blogs': blogs, 'filter': f})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})

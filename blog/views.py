from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Blog
from .models import Filter


# Create your views here.
def home(request):
    return render(request, 'blog/home.html')


def all_blogs(request):
    blogs = Blog.objects.all().order_by('-publish')
    f = Filter(request.GET, queryset=Blog.objects.all())
    return render(request, 'blog/all_blogs.html', {'blogs': blogs, 'filter': f})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})

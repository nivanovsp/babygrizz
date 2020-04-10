from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Blog
from .models import Filter
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
# Home view
def home(request):
    return render(request, 'blog/home.html')


# Blog views
def blog(request):
    blogs = Blog.objects.all()
    f = Filter(request.GET, queryset=Blog.objects.order_by('-publish')[:6])
    return render(request, 'blog/blog.html', {'blogs': blogs, 'filter': f})


def all_blogs(request):
    blogs = Blog.objects.all()
    f = Filter(request.GET, queryset=Blog.objects.all().order_by('-publish'))
    return render(request, 'blog/all_blogs.html', {'blogs': blogs, 'filter': f})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = blog.comments.filter(active=True)
    new_comment = None

    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = blog
            # Save the comment to the database
            new_comment.save()
            return HttpResponseRedirect(reverse('comment_success'))
    else:
        comment_form = CommentForm()
        comment_form.data['name', 'email', 'body'] = None

    return render(request, 'blog/detail.html',
                  {'blog': blog, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})


def comment_success(request):
    return render(request, 'blog/comment_success.html')


# Category views
def all_categories(request):
    blogs = Blog.objects.all()
    f = Filter(request.GET, queryset=Blog.objects.all().order_by('-publish'))
    return render(request, 'blog/all_categories.html', {'blogs': blogs, 'filter': f})


def category(request, category):
    if category == 'Category 1':
        blogs = Blog.objects.all()
        f = Filter(request.GET, queryset=Blog.objects.filter(category='Category 1').order_by('-publish'))
        category = Filter(request.GET, queryset=Blog.objects.filter(category='Category 1')[:1])
        return render(request, 'blog/category.html', {'blogs': blogs, 'filter': f, 'category': category})
    else:
        blogs = Blog.objects.all()
        f = Filter(request.GET, queryset=Blog.objects.filter(category='Category 2').order_by('-publish'))
        category = Filter(request.GET, queryset=Blog.objects.filter(category='Category 2')[:1])
        return render(request, 'blog/category.html', {'blogs': blogs, 'filter': f, 'category': category})


# User views
def author(request, user):
    if user == 1:
        blogs = get_object_or_404(Blog, pk=user)
        f = Filter(request.GET, queryset=Blog.objects.filter(user=1).order_by('-publish'))
        author = Filter(request.GET, queryset=Blog.objects.filter(user=1)[:1])
        return render(request, 'blog/author.html', {'blogs': blogs, 'filter': f, 'author': author})
    else:
        blogs = get_object_or_404(Blog, pk=user)
        f = Filter(request.GET, queryset=Blog.objects.filter(user=2).order_by('-publish'))
        author = Filter(request.GET, queryset=Blog.objects.filter(user=2)[:1])
        return render(request, 'blog/author.html', {'blogs': blogs, 'filter': f, 'author': author})

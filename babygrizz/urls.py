"""babygrizz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from blog import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.conf.urls import url

app_name = 'blog'

urlpatterns = [
    # Admin access
    path('admin/', admin.site.urls),

    # Blog pages
    path('', views.home, name='home'),
    path('home/contact_us/', views.contact_us, name='contact_us'),
    path('home/contact_success/', views.contact_success, name='contact_success'),
    path('blog/', views.blog, name='blog'),
    path('blog/all_blogs', views.all_blogs, name='all_blogs'),
    path('blog/all_categories', views.all_categories, name='all_categories'),
    path('blog/<str:category>/', views.category, name='category'),
    url(r'^list$', views.all_blogs),
    path('blog/blog/<int:blog_id>/', views.detail, name='detail'),
    path('blog/success', views.comment_success, name='comment_success'),
    path('blog/author/<int:user>/', views.author, name='author'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

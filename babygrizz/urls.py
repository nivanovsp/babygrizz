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
    path('blog/', views.blog, name='blog'),
    path('blog/all', views.all_blogs, name='all_blogs'),
    path('blog/category1/', views.cat_one, name='cat_one'),
    path('blog/category2/', views.cat_two, name='cat_two'),
    url(r'^list$', views.all_blogs),
    path('blog/<int:blog_id>/', views.detail, name='detail'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

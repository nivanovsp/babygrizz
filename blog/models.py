from django.db import models
from ckeditor.fields import RichTextField
import datetime
import django_filters
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=30)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='blog/images')
    video = EmbedVideoField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    publish = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} | {} | {} | {}'.format(self.title, self.category, self.created, self.publish)

    def published(self):
        tomorrow = datetime.date.today() + datetime.timedelta(1)
        return tomorrow > self.publish

    def blog_category(self, category):
        return category


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    message = models.TextField()
    sent_on = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    class Meta:
        ordering = ['sent_on']

    def __str__(self):
        return 'Contact {} by {}'.format(self.message, self.name)


# Create filters
class Filter(django_filters.FilterSet):
    category = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Blog
        fields = ['title', 'category']

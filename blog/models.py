from django.db import models
from ckeditor.fields import RichTextField
import datetime
import django_filters


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=30)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='blog/images')
    created = models.DateTimeField(auto_now_add=True)
    publish = models.DateField()

    def __str__(self):
        return '{} | {} | {} | {}'.format(self.title, self.category, self.created, self.publish)

    def published(self):
        tomorrow = datetime.date.today() + datetime.timedelta(1)
        return tomorrow > self.publish


# Create filters
class Filter(django_filters.FilterSet):
    category = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Blog
        fields = ['title', 'category']

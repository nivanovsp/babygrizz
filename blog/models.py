from django.db import models
from ckeditor.fields import RichTextField
import datetime

TYPES = (
    ('Category 1', 'Category 1'),
    ('Category 2', 'Category 2'),
    ('Category 3', 'Category 3'),
)


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=30, choices=TYPES)
    description = RichTextField(verbose_name='Description', null=True, blank=True)
    image = models.ImageField(upload_to='blog/images')
    created = models.DateTimeField(auto_now_add=True)
    publish = models.DateField()

    def __str__(self):
        return '{} | {} | {} | {}'.format(self.title, self.category, self.created, self.publish)

    def published(self):
        tomorrow = datetime.date.today() + datetime.timedelta(1)
        return tomorrow > self.publish

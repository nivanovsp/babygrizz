# Generated by Django 3.0.4 on 2020-03-30 11:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200330_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Code'),
        ),
    ]

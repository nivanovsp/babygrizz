# Generated by Django 3.0.4 on 2020-03-30 12:20

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200330_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='date',
        ),
        migrations.AddField(
            model_name='blog',
            name='date_edited',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=datetime.datetime(2020, 3, 30, 15, 20, 5, 933507)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('three', 'Category 3'), ('two', 'Category 2'), ('one', 'Category 1')], max_length=256),
        ),
    ]

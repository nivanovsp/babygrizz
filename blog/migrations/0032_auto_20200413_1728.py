# Generated by Django 3.0.4 on 2020-04-13 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_auto_20200413_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(),
        ),
    ]
# Generated by Django 3.1 on 2020-11-09 18:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Dashboard', '0010_auto_20201110_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='levelupdecisions',
            name='User',
        ),
        migrations.AddField(
            model_name='levelupdecisions',
            name='User',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 3.1 on 2020-11-09 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0003_userdetail_glevel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='father',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='mother',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='plus2board',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='plus2name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='slcboard',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='slcname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

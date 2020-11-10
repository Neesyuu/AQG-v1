# Generated by Django 3.1 on 2020-11-09 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Dashboard', '0005_auto_20201109_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='levelUpDecision',
            fields=[
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('percentage', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
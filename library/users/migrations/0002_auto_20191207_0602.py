# Generated by Django 3.0 on 2019-12-07 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='biography',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_of_death',
        ),
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]
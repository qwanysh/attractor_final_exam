# Generated by Django 3.0 on 2019-12-07 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20191207_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Date of birth'),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_death',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Date of death'),
        ),
    ]
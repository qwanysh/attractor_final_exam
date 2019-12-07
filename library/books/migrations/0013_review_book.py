# Generated by Django 3.0 on 2019-12-07 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_auto_20191207_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='book',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='books.Book', verbose_name='Book'),
        ),
    ]

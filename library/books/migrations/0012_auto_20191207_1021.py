# Generated by Django 3.0 on 2019-12-07 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0011_auto_20191207_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='books.Author', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='bookshelf',
            name='book',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bookshelfs', to='books.Book', verbose_name='Book'),
        ),
        migrations.AlterField(
            model_name='bookshelf',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bookshelfs', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default=None, max_length=500, verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
# Generated by Django 3.0 on 2019-12-07 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20191207_0726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100, verbose_name='Name')),
                ('year_of_publish', models.CharField(default=None, max_length=100, verbose_name='Year of publish')),
                ('file', models.FileField(blank=True, default=None, null=True, upload_to='book_files', verbose_name='File')),
                ('coverage', models.FileField(blank=True, default=None, null=True, upload_to='book_coverages', verbose_name='Coverage')),
                ('description', models.TextField(blank=True, default=None, null=True, verbose_name='Description')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.Author', verbose_name='Author')),
            ],
        ),
    ]

from django.db import models


class Author(models.Model):
    full_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default=None,
        verbose_name='Full name'
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name='Date of birth'
    )
    date_of_death = models.DateField(
        null=True,
        blank=True,
        verbose_name='Date of death'
    )
    biography = models.TextField(
        null=True,
        blank=True,
        default=None,
        verbose_name='Biography'
    )
    image = models.ImageField(
        null=True,
        blank=True,
        default=None,
        upload_to='author_images',
        verbose_name='Image'
    )

    def __str__(self):
        return self.full_name


class Book(models.Model):
    author = models.ForeignKey(
        'books.Author',
        on_delete=models.PROTECT,
        verbose_name='Author',
        related_name='books'
    )
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default=None,
        verbose_name='Name'
    )
    year_of_publish = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default=None,
        verbose_name='Year of publish'
    )
    file = models.FileField(
        null=True,
        blank=True,
        default=None,
        upload_to='book_files',
        verbose_name='File'
    )
    coverage = models.FileField(
        null=True,
        blank=True,
        default=None,
        upload_to='book_coverages',
        verbose_name='Coverage'
    )
    description = models.TextField(
        null=True,
        blank=True,
        default=None,
        verbose_name='Description'
    )

    def __str__(self):
        return self.name


class Bookshelf(models.Model):
    book = models.ForeignKey(
        'books.Book',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=None,
        verbose_name='Book',
        related_name='bookshelfs'
    )
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=None,
        verbose_name='User',
        related_name='bookshelfs'
    )

    def __str__(self):
        return f'{self.user.username} added {self.book.name}'


class Review(models.Model):
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='reviews',
        null=False,
        blank=False,
        default=None,
        verbose_name='User'
    )
    book = models.ForeignKey(
        'books.Book',
        on_delete=models.CASCADE,
        related_name='reviews',
        null=False,
        blank=False,
        default=None,
        verbose_name='Book'
    )
    text = models.TextField(
        max_length=500,
        null=False,
        blank=False,
        default=None,
        verbose_name='Text'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created at'
    )

    def __str__(self):
        return f'{self.user.username} - {self.text[:20]}'

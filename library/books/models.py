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
        default=None,
        verbose_name='Date of birth'
    )
    date_of_death = models.DateField(
        null=True,
        blank=True,
        default=None,
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

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    date_of_birth = models.DateField(
        verbose_name='Date of birth',
        null=True,
        blank=True,
        default=None
    )
    date_of_death = models.DateField(
        verbose_name='Date of death',
        null=True,
        blank=True,
        default=None
    )
    biography = models.TextField(
        verbose_name='Biography',
        max_length=500,
        null=True,
        blank=True,
        default=None
    )
    image = models.ImageField(
        verbose_name='Image',
        null=True,
        blank=True,
        default=None,
        upload_to='user_images',
    )

    def __str__(self):
        return self.username

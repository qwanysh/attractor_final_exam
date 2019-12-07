from django.forms import ModelForm

from .models import Author


class AuthorCreateForm(ModelForm):
    class Meta:
        model = Author
        exclude = []

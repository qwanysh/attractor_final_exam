from django import forms

from .models import Author


class AuthorCreateForm(forms.ModelForm):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control'
        })
    )
    date_of_death = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control'
        })
    )
    biography = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control'
        })
    )
    image = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control'
        })
    )

    class Meta:
        model = Author
        exclude = []

from django import forms

from .models import Author, Book, Review


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


class BookCreateForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    year_of_publish = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    file = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control'
        })
    )
    coverage = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control'
        })
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control'
        })
    )

    class Meta:
        model = Book
        exclude = ['author']


class ReviewCreateForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    class Meta:
        model = Review
        fields = ['text']

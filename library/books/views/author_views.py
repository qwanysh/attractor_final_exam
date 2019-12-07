from django.shortcuts import render
from django.views.generic import ListView

from ..models import Author


class AuthorListView(ListView):
    model = Author
    template_name = 'author/list.html'

from django.views.generic import ListView, DetailView

from ..models import Author


class AuthorListView(ListView):
    model = Author
    template_name = 'author/list.html'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author/detail.html'

from django.views.generic import ListView, DetailView

from ..models import Author
from ..forms import AuthorCreateForm


class AuthorListView(ListView):
    model = Author
    template_name = 'author/list.html'

    def get_context_data(self, **kwargs):
        kwargs['form'] = AuthorCreateForm()
        return super().get_context_data(**kwargs)


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author/detail.html'

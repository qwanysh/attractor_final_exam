from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

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


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author/create.html'
    form_class = AuthorCreateForm

    def get_success_url(self):
        return reverse('books:author_list')

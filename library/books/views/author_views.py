from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from ..models import Author
from ..forms import AuthorCreateForm


class AuthorListView(ListView):
    model = Author
    template_name = 'author/list.html'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author/detail.html'

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            kwargs['user_added_books'] = self.get_user_added_books
        return super().get_context_data(**kwargs)

    def get_user_added_books(self):
        books = []
        for bookshelf in self.request.user.bookshelfs.all():
            books.append(bookshelf.book)
        return books


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author/create.html'
    form_class = AuthorCreateForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Author has been added')
        return reverse('books:author_list')


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author/delete.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Author has been deleted')
        return reverse('books:author_list')

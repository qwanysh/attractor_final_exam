from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from ..models import Book, Author
from ..forms import BookCreateForm


class BookListView(ListView):
    model = Book
    template_name = 'book/list.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/detail.html'


class BookCreateView(CreateView):
    model = Book
    template_name = 'book/create.html'
    form_class = BookCreateForm

    def get_context_data(self, **kwargs):
        kwargs['author_pk'] = self.kwargs.get('pk')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.author = get_object_or_404(Author, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('books:book_list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book/delete.html'

    def get_success_url(self):
        return reverse('books:book_list')

from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from ..models import Book, Author
from ..forms import BookForm, ReviewCreateForm


class BookListView(ListView):
    model = Book
    template_name = 'book/list.html'

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            kwargs['user_added_books'] = self.get_user_added_books
        return super().get_context_data(**kwargs)

    def get_user_added_books(self):
        books = []
        for bookshelf in self.request.user.bookshelfs.all():
            books.append(bookshelf.book)
        return books


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/detail.html'

    def get_context_data(self, **kwargs):
        kwargs['form'] = ReviewCreateForm()
        kwargs['reviews'] = self.object.reviews.all().order_by('-created_at')
        return super().get_context_data(**kwargs)


class BookCreateView(UserPassesTestMixin, CreateView):
    model = Book
    template_name = 'book/create.html'
    form_class = BookForm

    def get_context_data(self, **kwargs):
        kwargs['author_pk'] = self.kwargs.get('pk')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.author = get_object_or_404(Author, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Book has been added')
        return reverse('books:book_detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user.is_superuser


class BookDeleteView(UserPassesTestMixin, DeleteView):
    model = Book
    template_name = 'book/delete.html'

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Book has been deleted')
        return reverse('books:book_list')

    def test_func(self):
        return self.request.user.is_superuser


class BookEditView(UserPassesTestMixin, UpdateView):
    model = Book
    template_name = 'book/edit.html'
    form_class = BookForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Book has been edited')
        return reverse('books:book_detail', kwargs={'pk': self.kwargs.get('pk')})

    def test_func(self):
        return self.request.user.is_superuser

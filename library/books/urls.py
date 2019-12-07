from django.urls import path
from .views import *

app_name = 'books'

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/new/', AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('authors/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),
    path('authors/<int:pk>/books/new', BookCreateView.as_view(), name='book_create'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('books/<int:pk>/add_to_bookshelf/', AddToBookshelfView.as_view(), name='book_add_bookshelf')
]

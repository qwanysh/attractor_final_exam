from django.urls import path
from .views import AuthorListView, AuthorDetailView, AuthorCreateView

app_name = 'books'

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/new/', AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
]

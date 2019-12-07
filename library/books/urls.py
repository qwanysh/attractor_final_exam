from django.urls import path
from .views import AuthorListView, AuthorDetailView, AuthorCreateView, AuthorDeleteView

app_name = 'books'

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/new/', AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('authors/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),
]

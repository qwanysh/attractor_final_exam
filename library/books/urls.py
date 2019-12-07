from django.urls import path
from .views import AuthorListView, AuthorDetailView

app_name = 'books'

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
]

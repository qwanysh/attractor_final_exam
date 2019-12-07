from django.urls import path
from .views import AuthorListView

app_name = 'books'

urlpatterns = [
    path('authors/<int:pk>/', AuthorListView.as_view(), name='author_list'),
]

from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import View

from ..models import Review


class ReviewCreateView(View):
    def post(self, request, *args, **kwargs):
        pass


class ReviewDeleteView(View):
    def get(self, request, *args, **kwargs):
        review = get_object_or_404(Review, pk=kwargs.get('pk'))
        review.delete()
        return redirect(reverse('books:book_detail', kwargs={'pk': kwargs.get('book_pk')}))

from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse
from django.views.generic import View

from ..forms import ReviewCreateForm
from ..models import Review, Book


class ReviewCreateView(View):
    def post(self, request, *args, **kwargs):
        form = ReviewCreateForm(data=request.POST)
        if form.is_valid():
            form.instance.user = self.request.user
            form.instance.book = get_object_or_404(Book, pk=kwargs.get('book_pk'))
            form.save()
        return redirect(reverse('books:book_detail', kwargs={'pk': kwargs.get('book_pk')}))


class ReviewDeleteView(View):
    def get(self, request, *args, **kwargs):
        review = get_object_or_404(Review, pk=kwargs.get('pk'))
        review.delete()
        return redirect(reverse('books:book_detail', kwargs={'pk': kwargs.get('book_pk')}))

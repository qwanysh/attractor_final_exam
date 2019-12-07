import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View

from ..models import Bookshelf, Book


class BookshelfView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body.decode())
        book = get_object_or_404(Book, pk=data.get('book_pk'))

        payload = {}

        try:
            bookshelf = Bookshelf.objects.get(book=book, user=self.request.user)
            bookshelf.delete()
            payload['result'] = 'deleted'
        except Bookshelf.DoesNotExist:
            Bookshelf.objects.create(book=book, user=self.request.user)
            payload['result'] = 'created'

        return JsonResponse(data=payload)

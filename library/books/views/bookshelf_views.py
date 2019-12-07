from django.http import JsonResponse
from django.views.generic import View


class BookshelfCreateView(View):
    def post(self, request, *args, **kwargs):
        payload = {
            'result': 'ok'
        }
        return JsonResponse(data=payload)


class BookshelfDeleteView(View):
    def post(self, request, *args, **kwargs):
        payload = {
            'result': 'ok'
        }
        return JsonResponse(data=payload)
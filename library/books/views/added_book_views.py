from django.http import JsonResponse
from django.views.generic import View


class AddToBookshelfView(View):
    def post(self, request, *args, **kwargs):
        payload = {
            'result': 'ok'
        }
        return JsonResponse(data=payload)

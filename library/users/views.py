from django.shortcuts import render

from django.views.generic import DetailView
from .models import User


class UserDetailView(DetailView):
    model = User
    template_name = 'user/detail.html'

    def get_queryset(self):
        return User.objects.all()

from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView, ListView
from .models import User
from .forms import UserLoginForm, UserRegisterForm


class UserDetailView(DetailView):
    model = User
    template_name = 'user/detail.html'

    def get_queryset(self):
        return User.objects.all()


class UserListView(ListView):
    model = User
    template_name = 'user/list.html'


class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(request.META.get('HTTP_REFERER'))


class UserLoginView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'form': UserLoginForm()
        }
        return render(request, 'user/login.html', context=context)

    def post(self, request, *args, **kwargs):
        context = {
            'form': UserLoginForm(data=request.POST)
        }
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('books:book_list')
        else:
            context['has_error'] = True
            return render(request, 'user/login.html', context=context)


class UserRegisterView(View):
    def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        context = {
            'form': form
        }
        return render(request, 'user/register.html', context=context)

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('books:book_list')
        else:
            context = {
                'form': form,
                'has_error': True
            }
            return render(request, 'user/register.html', context=context)

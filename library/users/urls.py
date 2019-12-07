from django.urls import path
from .views import UserDetailView, UserListView, UserLogoutView, UserLoginView, UserRegisterView

app_name = 'users'

urlpatterns = [
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('', UserListView.as_view(), name='list'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
]

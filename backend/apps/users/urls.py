from django.urls import path

from apps.users.views import UserListCreateAPIView, UserMeView

urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='users_list_create'),
    path('/me', UserMeView.as_view(), name='user_me'),
]

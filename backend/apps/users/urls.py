from django.urls import path

from apps.users.views import UserListCreateAPIView, UserMeView, UserBanView, UserUnBanView, UserToAdminView, \
    AdminToUserView

urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='users_list_create'),
    path('/me', UserMeView.as_view(), name='user_me'),

    path('/<int:pk>/ban', UserBanView.as_view(), name='user_ban'),
    path('/<int:pk>/unban', UserUnBanView.as_view(), name='user_unban'),
    path('/<int:pk>/to_admin', UserToAdminView.as_view(), name='user_to_admin'),
    path('/<int:pk>/to_user', AdminToUserView.as_view(), name='admin_to_user'),
]

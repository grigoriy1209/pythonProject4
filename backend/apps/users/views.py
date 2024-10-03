from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from django.contrib.auth import get_user_model

from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from apps.users.serializers import UserSerializer

# from core.dataclasses.user_dataclass import User

UserModel = get_user_model()


# class UserListCreateViewSet(ViewSet):
#
#     def list(self, request):
#         queryset = UserModel.objects.all()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = UserModel.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)


class UserListCreateAPIView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserMeView(GenericAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = [AllowAny,]

    def get(self, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserBanView(GenericAPIView):
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            user.is_active = False
            user.save()
        serializer = UserSerializer(user, )
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserUnBanView(GenericAPIView):
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            user.is_active = True
            user.save()
        serializer = UserSerializer(user, )
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserToAdminView(GenericAPIView):
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            user.is_staff = True
            user.save()
        serializer = UserSerializer(user, )
        return Response(serializer.data, status=status.HTTP_200_OK)


class AdminToUserView(GenericAPIView):
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            user.is_staff = False
            user.save()
        serializer = UserSerializer(user, )
        return Response(serializer.data, status=status.HTTP_200_OK)

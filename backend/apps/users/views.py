from rest_framework import status
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from django.contrib.auth import get_user_model

from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.users.serializers import UserSerializer

# from core.dataclasses.user_dataclass import User

UserModel = get_user_model()


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


from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from core.services.jwt_service import ActivateToken, JwtService

from apps.users.serializers import UserSerializer


class ActivateUserView(GenericAPIView):
    permission_classes = (AllowAny,)

    def patch(self, *args, **kwargs):
        token = kwargs['token']
        user = JwtService.verify_token(token,ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
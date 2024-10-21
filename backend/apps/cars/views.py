from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from .filters import CarFilter
from .models import CarModel
from .serializers import CarAddPhotoSerializer, CarSerializer


@method_decorator(name='get', decorator=swagger_auto_schema(security=[]))
class CarListCreateView(ListCreateAPIView):
    """
        Show all cars
    """
    queryset = CarModel.objects.all()
    # queryset = CarModel.objects.less_than_year(2023).only_audi()
    serializer_class = CarSerializer
    pagination_class = None
    filterset_class = CarFilter
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(auto_park_id=1)
        super().perform_create(serializer)


@method_decorator(name='get', decorator=swagger_auto_schema(security=[]))
@method_decorator(name='put', decorator=swagger_auto_schema(security=[]))
@method_decorator(name='patch', decorator=swagger_auto_schema(security=[]))
@method_decorator(name='delete', decorator=swagger_auto_schema(security=[]))
class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """"
    get:
        Get car id details
    put:
        Full Update car id details
    patch:
        Partial Update car id details
    delete:
        Delete car id
    """
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


# class CarAddPhotosView(UpdateAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = CarAddPhotoSerializer
#     queryset = CarModel.objects.all()
#     http_method_names = ('patch',)
#
#     def perform_update(self, serializer):
#         car = self.get_object()
#         car.photo.delete()
#         super().perform_update(serializer)

class CarAddPhotosView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CarModel.objects.all()

    def put(self, *args, **kwargs):
        files = self.request.FILES
        car = self.get_object()
        for index in files:
            serializer = CarAddPhotoSerializer(data={'photo': files[index]})
            serializer.is_valid(raise_exception=True)
            serializer.save(car=car)
        car_serializer = CarSerializer(car)
        return Response(car_serializer.data, status=status.HTTP_200_OK)

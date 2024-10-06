from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .filters import CarFilter
from .models import CarModel
from .serializers import CarAddPhotoSerializer, CarSerializer


class CarListView(ListAPIView):
    queryset = CarModel.objects.all()
    # queryset = CarModel.objects.less_than_year(2023).only_audi()
    serializer_class = CarSerializer
    pagination_class = None
    filterset_class = CarFilter
    permission_classes = (AllowAny,)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
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

    def put(self,  *args, **kwargs):
        files = self.request.FILES
        car = self.get_object()
        for index in files:
            serializer = CarAddPhotoSerializer(data={'photo': files[index]})
            serializer.is_valid(raise_exception=True)
            serializer.save(car=car)
        car_serializer = CarSerializer(car)
        return Response(car_serializer.data, status=status.HTTP_200_OK)


from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .filters import CarFilter
from .models import CarModel
from .serializers import CarSerializer


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

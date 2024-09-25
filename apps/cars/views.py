from rest_framework.generics import CreateAPIView, GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .filters import cars_filtered_queryset
from .models import CarModel
from .serializers import CarSerializer


class CarListView(CreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

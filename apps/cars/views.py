from django.forms import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CarModel


class CarListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        cars = [model_to_dict(car) for car in cars]
        return Response(cars, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = self.request.data
        car = CarModel.objects.create(**data)
        return Response(model_to_dict(car), status=status.HTTP_201_CREATED)


class CarRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(model_to_dict(car), status=status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        car.model = data['model']
        car.price = data['price']
        car.year = data['year']
        car.save()
        return Response(model_to_dict(car), status=status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            CarModel.objects.get(pk=pk).delete()
        except CarModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)

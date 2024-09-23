from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response

from .filters import cars_filtered_queryset
from .models import CarModel
from .serializers import CarSerializer


# class CarListCreateView(GenericAPIView):
#     # queryset = CarModel.objects.all()
#     # serializer_class = CarSerializer
#     # def get(self, *args, **kwargs):
#     #     cars = CarModel.objects.all()  # query_set
#     #     # cars = CarModel.objects.filter().get()  # queryset
#     #     # cars = cars.filter(model='Kia')
#     #     # cars = CarModel.objects.all().filter(Q (price__gte=111) | Q (model='kia'))
#     #     # cars = CarModel.objects.exclude(model='opel').count()
#     #     # cars = CarModel.objects.all().order_by('-id').reverse()
#     #     # cars = CarModel.objects.all()[2:4]
#     #     # cars = CarModel.objects.aggregate(Max('price'), Sum('year'),Avg('price'))
#     #     # cars = CarModel.objects.values('model').annotate(model_count=Count('model'))
#     #     serializer = CarSerializer(cars, many=True)
#     #     return Response(serializer.data)
#     #     # print(cars)
#     #     # return Response('ok')
#
class CarListCreateView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        return cars_filtered_queryset(self.request.query_params)

    # def get(self, *args, **kwargs):
    #     query = self.request.query_params
    #     cars = cars_filtered_queryset(query)
    #     serializer = CarSerializer(cars, many=True)
    #     return Response(serializer.data)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

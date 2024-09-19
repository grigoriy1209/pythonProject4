from rest_framework import serializers

from .models import CarModel


# class CarSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     model = serializers.CharField(max_length=100)
#     price = serializers.IntegerField()
#     year = serializers.IntegerField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#
#     def create(self, validated_data: dict):
#         car = CarModel.objects.create(**validated_data)
#         return car
#
#     def update(self, instance, validated_data):
#         for key, value in validated_data.items():
#             setattr(instance, key, value)
#             instance.save()
#             return instance
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'model', 'year', 'price', 'created_at', 'updated_at')

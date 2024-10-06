from rest_framework import serializers

from .models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = (
            "id",
            "model",
            "body_type",
            "year",
            "price",
            "created_at",
            "updated_at",
        )

    def validate(self, car):
        if car["model"] == "Kia":
            raise serializers.ValidationError({"model": "Kia is not available"})
        return car


class CarAddPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('photo',)
        extra_kwargs = {
            'photo': {
                       'required': True}
        }

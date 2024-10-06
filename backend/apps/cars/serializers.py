from rest_framework import serializers

from .models import CarModel, CarPhotoModel


class CarAddPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhotoModel
        fields = ('photo',)
        extra_kwargs = {
            'photo': {
                'required': True}
        }


class CarSerializer(serializers.ModelSerializer):
    photos = CarAddPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = CarModel
        fields = (
            "id",
            "model",
            "body_type",
            "year",
            "price",
            "photos",
            "created_at",
            "updated_at",
        )

    def validate(self, car):
        if car["model"] == "Kia":
            raise serializers.ValidationError({"model": "Kia is not available"})
        return car

from rest_framework import serializers

from better_profanity import profanity

from .models import CarModel

custom_words = ["Bich", "Petux"]
profanity.load_censor_words(custom_words)


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
        if profanity.contains_profanity(car["model"]):
            raise serializers.ValidationError(
                {"model": "The model name contains inappropriate language"}
            )
        return car

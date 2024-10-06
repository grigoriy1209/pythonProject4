from datetime import datetime

from django.core import validators as V
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.models import BaseModel

from apps.auto_parks.models import AutoParkModel
from apps.cars.choices import BodyTypeChoice
from apps.cars.regex import CarRegex

from .managers import CarManager
from .services import upload_car_photo


class CarModel(BaseModel):
    class Meta:
        db_table = "cars"

    model = models.CharField(
        max_length=50, validators=[V.RegexValidator(*CarRegex.MODEL.value)]
    )
    body_type = models.CharField(max_length=10, choices=BodyTypeChoice.choices)
    year = models.IntegerField(
        validators=[MinValueValidator(1990), MaxValueValidator(datetime.now().year)]
    )
    price = models.IntegerField(
        validators=[MinValueValidator(100), MaxValueValidator(1_000_000)]
    )
    auto_park = models.ForeignKey(
        AutoParkModel, on_delete=models.CASCADE, related_name="cars"
    )
    objects = CarManager()


class CarPhotoModel(BaseModel):
    class Meta:
        db_table = "car_photos"

    photo = models.ImageField(upload_to=upload_car_photo, blank=True)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name="photos")

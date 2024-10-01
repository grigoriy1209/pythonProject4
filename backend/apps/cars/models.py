from datetime import datetime

from django.core import validators as V
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.managers import CarManager
from core.models import BaseModel

from apps.auto_parks.models import AutoParkModel
from apps.cars.choices import BodyTypeChoice
from apps.cars.regex import CarRegex


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

from django.db import models

from core.models import BaseModel

from apps.auto_parks.models import AutoParkModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'

    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE,related_name='cars')

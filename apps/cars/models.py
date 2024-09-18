from django.db import models

from core.models import BaseModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'

    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()

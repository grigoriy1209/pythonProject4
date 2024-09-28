from django.db import models


class BodyTypeChoice(models.TextChoices):
    Hatchback = "Hatchback"
    Sedan = "Sedan"
    Coupe = "Coupe"
    Jeep = "Jeep"
    Wagon = "Wagon"

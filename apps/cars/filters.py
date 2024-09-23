from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from apps.cars.models import CarModel


def cars_filtered_queryset(query: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()

    for key, value in query.items():
        match key:
            case 'price_gt':
                qs = qs.filter(price__gt=value)
            case 'price_gte':
                qs = qs.filter(price__gte=value)
            case 'price_lt':
                qs = qs.filter(price__lt=value)
            case 'price_lte':
                qs = qs.filter(price__lte=value)
            case 'price_eq':
                qs = qs.filter(price=value)
            case 'model':
                qs = qs.filter(model=value)
            case 'model':
                qs = qs.filter(model__in=value)
            case 'model':
                qs = qs.filter(model__icontains=value)
            case 'model':
                qs = qs.filter(model__contains=value)
            case 'model':
                qs = qs.filter(model__iendswith=value)

            case _:
                raise ValidationError(f"Invalid value for {key}")
    return qs



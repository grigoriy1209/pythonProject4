from django_filters import rest_framework as filters

from apps.cars.choices import BodyTypeChoice


class CarFilter(filters.FilterSet):
    lt = filters.NumberFilter(field_name='year', lookup_expr='lt')
    range = filters.NumberFilter(field_name='year', lookup_expr='range')  # min-max
    year_in = filters.BaseInFilter(field_name='year',)
    body_type = filters.ChoiceFilter(field_name='body_type', choices=BodyTypeChoice.choices)
    model_start = filters.CharFilter(field_name='model', lookup_expr='startswith')
    order = filters.OrderingFilter(
        fields=(
            'id',
            'body_type',
            'model',
            'price',
        )
    )
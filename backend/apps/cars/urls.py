from django.urls import path

from .views import CarListView, CarRetrieveUpdateDestroyView, CarAddPhotoView

urlpatterns = [
    path("", CarListView.as_view(), name="car_list"),
    path(
        "/<int:pk>",
        CarRetrieveUpdateDestroyView.as_view(),
        name="car_retrieve_update_delete",
    ),
    path("/<int:pk>/photos", CarAddPhotoView.as_view(), name="car_add_photo"),
]

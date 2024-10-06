import os
from uuid import uuid1


def upload_car_photo(instance, file: str) -> str:
    extension = file.split('.')[-1]
    return os.path.join(instance.car.auto_park.name, 'car_photos', f'{uuid1()}.{extension}')

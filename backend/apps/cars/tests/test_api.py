from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase

from apps.auto_parks.models import AutoParkModel
from apps.cars.models import CarModel

UserModel = get_user_model()


class CarAPITestCase(APITestCase):
    def setUp(self):
        self.auto_park_id = AutoParkModel.objects.create(
            name='AutoPark1'
        ).id
        self.car1 = CarModel.objects.create(
            model='BMW',
            body_type='Jeep',
            price=2000,
            year=2000,
            auto_park_id=self.auto_park_id
        )
        self.car2 = CarModel.objects.create(
            model='Audi',
            body_type='Jeep',
            price=2000,
            year=2001,
            auto_park_id=self.auto_park_id
        )

    def test_get_all_cars(self):
        res = self.client.get(reverse('car_create_list'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        data = res.data
        self.assertEqual(len(data), 2)
        CarModel.objects.get(pk=self.car1.id)
        self.assertEqual(CarModel.objects.get(pk=self.car1.id).model, 'BMW')
        CarModel.objects.get(pk=self.car2.id)
        self.assertEqual(CarModel.objects.get(pk=self.car2.id).model, 'Audi')

    def _authenticate(self):
        user = UserModel.objects.create_user(
            email='fake@gmail.com',
            password='Password1@',
            is_active=True,
        )
        res = self.client.post(reverse('auth_login'), {'email': user.email, 'password': 'Password1@'})
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + res.data['access'])
        print(UserModel.objects.all()[0].__dict__)

    def test_create_car_without_auth(self):
        data = {
            'model': 'Oka',
            'body_type': 'Jeep',
            'price': 2000,
            'year': 2000,
        }
        count_before = CarModel.objects.count()
        response = self.client.post(reverse('car_create_list'), data)
        count_after = CarModel.objects.count()
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(count_before, count_after)

    def test_create_car_with_auth(self):
        self._authenticate()
        data = {
            'model': 'Oka',
            'body_type': 'Jeep',
            'price': 2000,
            'year': 2000,
        }
        count_before = CarModel.objects.count()
        response = self.client.post(reverse('car_create_list'), data)
        count_after = CarModel.objects.count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual( count_after, count_before + 1 )

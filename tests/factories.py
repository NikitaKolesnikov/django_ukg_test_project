import factory
from apps.restaurant.models import Restaurant


class RestaurantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Restaurant

    name: str = factory.Faker('name')
    description: str

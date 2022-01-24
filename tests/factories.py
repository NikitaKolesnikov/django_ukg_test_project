import factory
from apps.restaurant.models import Restaurant


class RestaurantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Restaurant

    name: str = factory.Sequence(lambda n: 'FACTORY_TEST_SLUG%d' % n)
    description: str

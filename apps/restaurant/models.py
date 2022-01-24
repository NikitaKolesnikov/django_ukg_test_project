from django.db import models
from django.utils.translation import gettext as _


class RestaurantManager(models.Manager):
    pass

class Restaurant(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'))

    objects = RestaurantManager()

    class Meta:
        verbose_name = _('Restaurant')
        verbose_name_plural = _('Restaurants')

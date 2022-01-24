from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _


class Restaurant(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'))
    slug = models.SlugField(
        max_length=150,
        default=None,
        null=True,
        blank=True,
        verbose_name='Slug',
        unique=True,
    )

    class Meta:
        verbose_name = _('Restaurant')
        verbose_name_plural = _('Restaurants')
        ordering = ['-id']

    def save(self, **kwargs) -> None:
        if self.name and self.slug is None:
            self.slug = slugify(self.name)
        super().save(**kwargs)

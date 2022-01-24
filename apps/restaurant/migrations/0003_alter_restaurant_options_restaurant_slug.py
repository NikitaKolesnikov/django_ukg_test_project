# Generated by Django 4.0.1 on 2022-01-24 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_restaurant_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurant',
            options={'ordering': ['-id'], 'verbose_name': 'Restaurant', 'verbose_name_plural': 'Restaurants'},
        ),
        migrations.AddField(
            model_name='restaurant',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=150, null=True, unique=True, verbose_name='Slug'),
        ),
    ]
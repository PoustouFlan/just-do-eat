from django.db import models

from ingredients.models import Ingredient


class Recipe(models.Model):
    ingredients = models.ManyToManyField(Ingredient)
    url = models.CharField(max_length=512)
    name = models.CharField(max_length=256)
    gluten_free = models.BooleanField(default=False)
    lactose_free = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    pork_free = models.BooleanField(default=False)
    sweet = models.BooleanField(default=False)
    salty = models.BooleanField(default=False)

    def __str__(self):
        return self.url

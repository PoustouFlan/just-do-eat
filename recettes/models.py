from django.db import models

from ingredients.models import Ingredient


class Recipe(models.Model):
    ingredients = models.ManyToManyField(Ingredient)
    url = models.URLField()
    gluten_free = models.BooleanField()
    lactose_free = models.BooleanField()
    vegetarian = models.BooleanField()
    vegan = models.BooleanField()
    pork_free = models.BooleanField()
    sweet = models.BooleanField()
    salty = models.BooleanField()

    def __str__(self):
        return self.url

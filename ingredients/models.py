from datetime import datetime
from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class PossessedIngredient(models.Model):
    quantity = models.PositiveIntegerField(default=1)
    expire_date = models.DateTimeField(default=datetime.now)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantity}x {self.ingredient.name} ({self.expire_date})"

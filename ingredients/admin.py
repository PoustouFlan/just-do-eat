from django.contrib import admin
from ingredients.models import Ingredient, PossessedIngredient


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(PossessedIngredient)
class PossessedIngredientAdmin(admin.ModelAdmin):
    pass

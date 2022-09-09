from django.contrib import admin
from recettes.models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_filter = (
        "gluten_free",
        "lactose_free",
        "vegetarian",
        "vegan",
        "pork_free",
        "sweet",
        "salty",
    )

from django.contrib import admin
from ingredients.models import Ingredient, PossessedIngredient
from django.http.request import HttpRequest
from django.db.models.query import QuerySet
from pickle import load as pickle_load


FILE = "data/save.p"


def load(filename: str) -> dict:
    save = pickle_load(open(filename, "rb"))
    return save


def uses_only(save: dict, ingredients: list[PossessedIngredient]):
    """
    Yields every recipes that uses only some ingredients
    """
    for url, recipe in save.items():
        for ingredient_object in ingredients:
            if ingredient_object.ingredient.name not in recipe["ingredients"]:
                break
        else:
            yield url


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(PossessedIngredient)
class PossessedIngredientAdmin(admin.ModelAdmin):

    actions = ("get_uses_only",)
    autocomplete_fields = ("ingredient",)
    list_filter = ("expire_date",)

    @admin.action(description="Recettes possibles en utilisant seulement ces ingrédients")
    def get_uses_only(self, request: HttpRequest, queryset: QuerySet):
        content = load(FILE)
        for url in uses_only(content, queryset.all()):
            print(url)

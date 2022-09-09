import logging
import random
from typing import Iterator

from django.contrib import admin
from ingredients.models import Ingredient, PossessedIngredient
from recettes.models import Recipe
from django.http import HttpRequest, HttpResponse
from django.db.models.query import QuerySet
from django.template import loader

from pickle import load as pickle_load

log = logging.getLogger(__name__)


FILE = "data/save.p"


def load(filename: str) -> dict:
    save = pickle_load(open(filename, "rb"))
    return save


def uses_only(save: dict, ingredients: list[PossessedIngredient]) -> Iterator[Recipe]:
    """
    Yields every recipes that uses only some ingredients
    """
    for url, recipe in save.items():
        ingredients_objects: list[Ingredient] = []
        for ingredient_object in ingredients:
            if ingredient_object.ingredient.name not in recipe["ingredients"]:
                break
            ingredients_objects.append(ingredient_object.ingredient)
        else:
            recipe_object, created = Recipe.objects.get_or_create(url=url)
            recipe_object: Recipe
            ingredients_list_but_for_real = [
                Ingredient.objects.get_or_create(name=x)[0] for x in recipe["ingredients"]
            ]
            recipe_object.ingredients.set(ingredients_list_but_for_real)
            recipe_object.gluten_free = recipe["isGlutenFree"]
            recipe_object.lactose_free = recipe["isLactoseFree"]
            recipe_object.vegetarian = recipe["isVegetarian"]
            recipe_object.vegan = recipe["isVegan"]
            recipe_object.pork_free = recipe["isPorkFree"]
            recipe_object.sweet = recipe["isSweet"]
            recipe_object.salty = recipe["isSalty"]
            recipe_object.name = recipe["title"]
            recipe_object.save()
            yield recipe_object


def generate_meal_list(save: dict, ingredients: list[PossessedIngredient]) -> Iterator[Recipe]:
    k = 7
    bought = []
    ingredients = [x.ingredient.name for x in ingredients]
    done = set()
    for _ in range(k):
        best = None
        cost = float('inf')
        keys = list(save.keys())
        random.shuffle(keys)
        for url in keys:
            recipe = save[url]
            if url in done:
                continue
            using = recipe['ingredients']
            if len(using) < 2:
                continue
            this_cost = 0
            for ingredient in using:
                if ingredient not in ingredients and ingredient not in bought:
                    this_cost += 1
            if this_cost < cost:
                cost = this_cost
                best = url
                recipe_object, created = Recipe.objects.get_or_create(url=url)
                recipe_object: Recipe
                if created:
                    ingredients_list_but_for_real = [
                        Ingredient.objects.get_or_create(name=x)[0] for x in recipe["ingredients"]
                    ]
                    print(len(ingredients_list_but_for_real))
                    recipe_object.ingredients.set(ingredients_list_but_for_real)
                    recipe_object.gluten_free = recipe["isGlutenFree"]
                    recipe_object.lactose_free = recipe["isLactoseFree"]
                    recipe_object.vegetarian = recipe["isVegetarian"]
                    recipe_object.vegan = recipe["isVegan"]
                    recipe_object.pork_free = recipe["isPorkFree"]
                    recipe_object.sweet = recipe["isSweet"]
                    recipe_object.salty = recipe["isSalty"]
                    recipe_object.name = recipe["title"]
                    recipe_object.save()
                    print("Created object %s", recipe_object)
        yield recipe_object
        done.add(best)
        for ingredient in save[best]:
            if ingredient not in ingredients and ingredient not in bought:
                bought.append(ingredient)


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
        recipes = list(uses_only(content, queryset.all()))
        template = loader.get_template("recettes/recipes.html")
        print(len(recipes))
        context = {"recipes": recipes}
        return HttpResponse(template.render(context, request))

    @admin.action(description="Liste de recettes pour les 7 prochains jours")
    def get_uses_only(self, request: HttpRequest, queryset: QuerySet):
        content = load(FILE)
        recipes = list(generate_meal_list(content, queryset.all()))
        template = loader.get_template("recettes/recipes.html")
        print(len(recipes))
        context = {"recipes": recipes}
        return HttpResponse(template.render(context, request))

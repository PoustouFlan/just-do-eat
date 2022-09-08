from django.contrib import admin
from recettes.models import Recipe


@admin.register(Recipe)
class RecipyAdmin(admin.ModelAdmin):
    pass

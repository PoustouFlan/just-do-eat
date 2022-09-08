from justdoeat import Justdoeat
from marmiton import Marmiton

save = Justdoeat.load("data/save.p")

print("3 recettes aléatoires :")
for url in Justdoeat.random_recipes(save, 3):
    print(Marmiton.title_of_url(url))
print()

ingredients = (
    'beurre',
    'sel',
    'sucre',
    'eau',
    'tomate',
    'oignon',
    'ail',
    'poivre',
    'persil',
    'thym',
    'chair à saucisse',
    'lait',
    'muscade',
    'pomme de terre',
    'crème',
)
print("Toutes les recettes que vous pouvez faire en n'utilisant seulement ces"
      "ingrédients:", ', '.join(ingredients))
for url in Justdoeat.uses_only(save, ingredients):
    print(Marmiton.title_of_url(url))
print()

ingredients = (
    'chair à saucisse',
    'pomme de terre',
    'courgette',
)
print("Toutes les recettes qui utilisent chacun de ces ingrédients:",
        ', '.join(ingredients))
for url in Justdoeat.uses(save, ingredients):
    print(Marmiton.title_of_url(url))

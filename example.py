from tools.justdoeat import Justdoeat
from tools.marmiton import Marmiton

save = Justdoeat.load("data/save.p")
filtered = Justdoeat.filter(save, isVegan=True)

print("3 recettes végan aléatoires :")
for url in Justdoeat.random_recipes(filtered, 3):
    recipe = filtered[url]
    print(recipe['title'])
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
print("Toutes les recettes que vous pouvez faire en utilisant seulement ces"
      " ingrédients:", ', '.join(ingredients))
for url in Justdoeat.uses_only(save, ingredients):
    recipe = save[url]
    print(recipe['title'])
print()

ingredients = (
    'chair à saucisse',
    'pomme de terre',
    'courgette',
)
print("Toutes les recettes qui utilisent chacun de ces ingrédients:",
        ', '.join(ingredients))
for url in Justdoeat.uses(save, ingredients):
    recipe = save[url]
    print(recipe['title'])
print()

filtered = Justdoeat.filter(save, isPorkFree=True)
print("7 recettes sans porc qui ne nécessiteraient pas beaucoup d'achats"
        " supplémentaires")
for url in Justdoeat.minimum_buy(filtered, ingredients, 7):
    recipe = filtered[url]
    print(recipe['title'])

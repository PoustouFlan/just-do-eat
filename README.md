# Just Do Eat !
##### Minimum Viable Code as a Proof of Concept

Python Proof of Concept for getting recipes from ingredients only

### Usage / Example :
```python
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

print("10 recettes qui ne nécessiteeraient pas beaucoup d'achats"
        " supplémentaires")
for url in Justdoeat.minimum_buy(save, ingredients, 10):
    print(Marmiton.title_of_url(url))
print()
```

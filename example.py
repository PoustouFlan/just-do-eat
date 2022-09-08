from justdoeat import Justdoeat
from marmiton import Marmiton

save = Justdoeat.load("data/save.p")

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

for url in Justdoeat.uses_only(save, ingredients):
    url = "https://www.marmiton.org" + url
    query_result = Marmiton.get(url)
    recipe = Marmiton.extract_recipe(query_result)
    print(recipe['title'])

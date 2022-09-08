from marmiton import Marmiton
from pickle import load, dump
from os import system

class Justdoeat(object):

    @staticmethod
    def get_recipes(n = float('inf')):
        i = 0
        for recipe in Marmiton.all_recipe():
            i += 1
            ingredients = list(Marmiton.ingredients(recipe))
            yield (recipe['url'], ingredients)
            if i >= n:
                break

    @staticmethod
    def save_recipes(filename, n = float('inf')):
        for url, ingredients in Justdoeat.get_recipes(n):
            system(f"cp {filename} {filename}.back")
            try:
                save = load(open(filename, 'rb'))
            except FileNotFoundError:
                save = {}
            save[url] = ingredients
            dump(save, open(filename, 'wb'))


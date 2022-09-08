from marmiton import Marmiton
from random import randint
from pickle import load as pickle_load, dump as pickle_dump
from os import system

class Justdoeat(object):

    @staticmethod
    def load(filename):
        save = pickle_load(open(filename, 'rb'))
        return save

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
                save = load(filename)
            except FileNotFoundError:
                save = {}
            save[url] = ingredients
            pickle_dump(save, open(filename, 'wb'))

    @staticmethod
    def uses_only(save, ingredients):
        for url, using in save.items():
            for ingredient in using:
                if ingredient not in ingredients:
                    break
            else:
                yield url

    @staticmethod
    def random_recipes(save, n=1):
        save = list(save.items())
        max_bound = len(save) - 1
        indices = set()
        while len(indices) < n:
            i = randint(0, max_bound)
            if i in indices:
                continue
            url = save[i][0]
            yield url
            indices.add(url)


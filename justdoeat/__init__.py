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
            yield Marmiton.simplified_json(recipe)
            if i >= n:
                break

    @staticmethod
    def save_recipes(filename, n = float('inf')):
        for recipe in Justdoeat.get_recipes(n):
            system(f"cp {filename} {filename}.back")
            try:
                save = Justdoeat.load(filename)
            except FileNotFoundError:
                save = {}
            save.update(recipe)
            pickle_dump(save, open(filename, 'wb'))

    @staticmethod
    def uses_only(save, ingredients):
        """
        Yields every recipes that uses only some ingredients
        """
        for url, using in save.items():
            for ingredient in using:
                if ingredient not in ingredients:
                    break
            else:
                yield url

    @staticmethod
    def uses(save, ingredients):
        """
        Yields every recipes that uses each of the required ingredients
        """
        for url, using in save.items():
            for ingredient in ingredients:
                if ingredient not in using:
                    break
            else:
                yield url

    @staticmethod
    def random_recipes(save, n=1):
        """
        Yields n random recipes
        """
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

    @staticmethod
    def minimum_buy(save, ingredients, k=1):
        """
        Yields k differents recipes which needs a fairly small amount of
        ingredients to buy.
        Note : this is equivalent to the "Minimum K-Union" problem, which is
        NP-Complete, so the solution cannot be proven to be optimal.
        """
        bought = []
        done = set()
        for _ in range(k):
            best = None
            cost = float('inf')
            for url, using in save.items():
                if url in done:
                    continue
                this_cost = 0
                for ingredient in using:
                    if ingredient not in ingredients and ingredient not in bought:
                        this_cost += 1
                if this_cost < cost:
                    cost = this_cost
                    best = url
            yield best
            done.add(best)
            for ingredient in save[best]:
                if ingredient not in ingredients and ingredient not in bought:
                    bought.append(ingredient)

    @staticmethod
    def filter(save, **criterias):
        filtered = {}
        for url, recipe in save.items():
            if type(recipe) == list:
                continue
            for criteria, value in criterias.items():
                if recipe[criteria] != value:
                    break
            else:
                filtered[url] = recipe
        return filtered

        


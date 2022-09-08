from marmiton import Marmiton
from pickle import dump

class Justdoeat(object):

    @staticmethod
    def get_recipes(n):
        save = {}
        i = 0
        for recipe in Marmiton.all_recipe():
            i += 1
            ingredients = list(Marmiton.ingredients(recipe))
            save[recipe['url']] = ingredients
            print(round(100*i/n, 2), '%')
            if i >= n:
                break
        return save

    @staticmethod
    def save_recipes(filename, n = float('inf')):
        save = Justdoeat.get_recipes(n)
        dump(save, open(filename, 'wb'))



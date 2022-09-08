# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import urllib.parse
import urllib.request

import re
import json


class RecipeNotFound(Exception):
    pass


class Marmiton(object):

    @staticmethod
    def get(url):
        """
        Get json from Marmiton url
        """
        try:
            html_content = urllib.request.urlopen(url).read()
        except urllib.error.HTTPError as e:
            raise RecipeNotFound if e.code == 404 else e
        soup = BeautifulSoup(html_content, 'html.parser')        
        return json.loads(soup.find('script', type='application/json').string)

    @staticmethod
    def search(query_dict):
        """
        Search recipes parsing the returned html data.
        Options:
        'aqt': string of keywords separated by a white space  (query search)
        Optional options :
        'dt': "entree" | "platprincipal" | "accompagnement" | "amusegueule" | "sauce"  (plate type)
        'exp': 1 | 2 | 3  (plate expense 1: cheap, 3: expensive)
        'dif': 1 | 2 | 3 | 4  (recipe difficultie 1: easy, 4: advanced)
        'veg': 0 | 1  (vegetarien only: 1)
        'rct': 0 | 1  (without cook: 1)
        'sort': "markdesc" (rate) | "popularitydesc" (popularity) | "" (empty for relevance)
        """
        base_url = "https://www.marmiton.org/recettes/recherche.aspx?"
        page = 1
        while True:
            query_dict["page"] = page
            query_url = urllib.parse.urlencode(query_dict)
            url = base_url + query_url
            try:
                query_result = Marmiton.get(url)
            except RecipeNotFound:
                break
            yield from Marmiton.extract_recipes(query_result)
            page += 1

    @staticmethod
    def ingredients(recipe):
        """
        Returns every ingredients needed for a recipe
        """
        for ingredientGroup in recipe['ingredientGroups']:
            for ingredient in ingredientGroup['items']:
                yield ingredient['name']
        

    @staticmethod
    def recipes_url(url):
        """
        Returns urls of every recipe proposed in the page
        """
        base_url = "https://www.marmiton.org/recettes"
        url = base_url + url
        try:
            html_content = urllib.request.urlopen(url).read()
        except urllib.error.HTTPError as e:
            raise RecipeNotFound if e.code == 404 else e
        soup = BeautifulSoup(html_content, 'html.parser')        
        recipes = soup.find_all("a", {"class":"recipe-card-link"})
        return map(lambda recipe: recipe['href'], recipes)

    @staticmethod
    def extract_recipe(query_result):
        """
        Returns recipe json from page query (get)
        """
        return query_result['props']['pageProps']['recipeData']['recipe']

    @staticmethod
    def extract_recipes(query_result):
        """
        Returns every recipes json from search query (search)
        """
        recipes = []
        results = query_result['props']['pageProps']['searchResults']['hits']
        for result in results:
            if result['contentType'] == "RECIPE":
                recipes.append(result)
        return recipes

    @staticmethod
    def all_recipe():
        """
        Get every existing Marmiton recipes
        """
        i = 0
        done = False
        while not done:
            done = True
            i += 1
            uri = f"?type=platprincipal&page={i}"
            for url in Marmiton.recipes_url(uri):
                done = False
                query_result = Marmiton.get(url)
                recipe = Marmiton.extract_recipe(query_result)
                yield recipe




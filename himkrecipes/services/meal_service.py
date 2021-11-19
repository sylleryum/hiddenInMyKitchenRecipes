from collections import Counter

from himkrecipes.utils import api_call

ENDPOINT = "https://www.themealdb.com/api/json/v1/1/"
GET_MEAL = ENDPOINT + "lookup.php?i="
SAMPLE_MEAL = "52772"

SEARCH_CATEGORY = ENDPOINT + "filter.php?c="
SEARCH_INGREDIENT = ENDPOINT + "filter.php?i="
SEARCH_AREA = ENDPOINT + "filter.php?a="

GET_INGREDIENTS = ENDPOINT + "list.php?i=list"
KEY_INGREDIENT = "strIngredient"
ORDER_INGREDIENT = "strIngredient"

CATEGORY_CATEGORIES = 1
CATEGORY_COUNTRY = 2
CATEGORY_INGREDIENTS = 3


def get_recipe(recipe_id: int):
    response = api_call.get(GET_MEAL + str(recipe_id))
    json_response = response.json()['meals'][0]

    return json_response


def get_all_ingredients(keys, order):
    result: list = api_call.get(GET_INGREDIENTS).json()['meals']
    if keys == KEY_INGREDIENT:
        result = list(map(lambda x: (x['strIngredient']), result))
    if order == ORDER_INGREDIENT:
        result.sort()
    return result


# def search_ingredients(ingredients: list):
#     # retrieves all recipe search items from first ingredient
#     search_result = __search(CATEGORY_INGREDIENTS, ingredients[0])
#     result_recipes = []
#     # only ingredients>0 will be used now to check recipes above
#     ingredients.pop(0)
#     if search_result is None:
#         return None
#
#     # check ingredients>0 if present on the recipes found from ingredients[0]
#     for rec in search_result:
#         # recipe found from ingredient[0]
#         full_recipe = get_recipe(rec["idMeal"])
#         if len(ingredients) == 0:
#             return result_recipes.append(full_recipe)
#
#         # get ingredients from recipe (maximum ingredients = 20)
#         recipe_ingredients = []
#         for i in range(19):
#             if full_recipe["strIngredient" + str(i + 1)] == '':
#                 break
#             recipe_ingredients.append(full_recipe["strIngredient" + str(i + 1)])
#         #
#
#         for k, received_ingredients in enumerate(ingredients):
#             print()
#             if received_ingredients.upper() not in (ing.upper() for ing in recipe_ingredients):
#                 break
#             elif k == len(ingredients) - 1:
#                 result_recipes.append(full_recipe)
#
#     print()
#         #     if
#     # recipes = __search(CATEGORY_INGREDIENTS, ingredients[0])
#
#     return result_recipes

# def search_ingredients(ingredients: list):
#     # retrieves all recipe search items from first ingredient
#     # search_result = __search(CATEGORY_INGREDIENTS, ingredients[0])
#     search_results = list(map(lambda x: __search(CATEGORY_INGREDIENTS, x), ingredients))
#     # init_list = search_results[0]
#     # search_results.pop(0)
#     if None in search_results or len(search_results) == 1:
#         return None
#
#     # shortest_list = min(search_results, key=len)
#     # search_results.remove(shortest_list)
#     # matches = {}
#     # for recipe_major in search_results:
#     #     for recipe_minor in shortest_list:
#     #         if recipe_minor in recipe_major:
#     #             matches[recipe_minor['idMeal']] = +1
#     #             print()
#     # res = [x for l in search_results for x in l]
#     ll = []
#     for i in search_results:
#         for inner in i:
#             ll.append(inner['idMeal'])
#
#     c = Counter(ll)
#     to_return = []
#     for final in c.items():
#         if final[1] == len(search_results):
#             to_return.append(final[0])
#     print()

def search_ingredients(ingredients: list):
    init_list, search_list = _fetch_ingredients(ingredients)
    final_result = _match_ingredients(init_list, search_list, ingredients)
    return final_result


def _match_ingredients(init_list, search_list, ingredients):
    if len(init_list) == 0 or len(search_list) + 1 < len(ingredients):
        return []
    if len(search_list) == 0:
        return init_list

    final_result = []
    for i, to_search in enumerate(search_list):
        for recipe in init_list:
            if recipe not in to_search:
                continue
            if recipe in to_search and i == len(search_list) - 1:
                final_result.append(recipe)
    return final_result


def _fetch_ingredients(ingredients: list):
    search_list = []
    init_list = []
    for ing in ingredients:
        result = _search(CATEGORY_INGREDIENTS, ing.strip())
        if result is not None and (len(init_list) == 0 or len(result) < len(init_list)):
            init_list = result
        search_list.append(result)

    search_list = list(filter(lambda x: x is not None, search_list))
    if len(search_list) == 0:
        return [], []

    search_list.remove(init_list)
    return init_list, search_list


def _search(category, param: str):
    if category == CATEGORY_INGREDIENTS:
        result = api_call.get(SEARCH_INGREDIENT + param).json()['meals']
        return result

    return None

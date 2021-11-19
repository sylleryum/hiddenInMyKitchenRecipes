from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

# @permission_classes([IsAuthenticated])
# @permission_classes([])
# class GetRecipe(GenericAPIView):
#     name = 'get-recipe'
#
#     def get(self, request, *args, **kwargs):
#         the_return = meal_service.get_recipe(kwargs['id'])
#
#         # translate
#         instructions = the_return['strInstructions']
#         translated = translate_service.translate(instructions, 'pt')
#
#         return Response(data=the_return, status=status.HTTP_200_OK)


# @permission_classes([IsAuthenticated])
from himkrecipes.services import meal_service, translate_service


@api_view(['GET'])
def get_recipe(request, recipe_id):
    the_return = meal_service.get_recipe(recipe_id)

    # translate
    instructions = the_return['strInstructions']
    translated = translate_service.translate(instructions, 'pt')

    return Response(data=the_return, status=status.HTTP_200_OK)


@api_view(['GET'])
def search_ingredients(request):
    if "ingredients" not in request.query_params:
        return Response(data={"ErrorMessage": "no param passed"}, status=status.HTTP_400_BAD_REQUEST)

    ingredients = request.query_params['ingredients'].split(',')

    result = meal_service.search_ingredients(ingredients=ingredients)
    wrapper = {'total': len(result),
               'recipe_endpoint:': '/recipe/{idMeal}',
               'results': result}

    return Response(data=wrapper, status=status.HTTP_200_OK)


@api_view(['get'])
def get_all_ingredients(request):
    # if 'keys' in request.query_params:
    result = meal_service.get_all_ingredients(request.query_params.dict().get('keys'),
                                              request.query_params.dict().get('order'))
    # else:
    #     result = meal_service.get_all_ingredients(request.query_params['keys'])

    wrapper = {'total': len(result),
               'results': result}
    return Response(data=wrapper, status=status.HTTP_200_OK)

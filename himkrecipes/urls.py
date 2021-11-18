"""recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from himkrecipes.views import get_recipe, search_ingredients, get_all_ingredients

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('recipe/<int:id>', views.GetRecipe.as_view(),
    #      name=views.GetRecipe.name),
    path('recipe/<int:recipe_id>', get_recipe, name='get_recipe'),
    path('search', search_ingredients, name='search_ingredients'),
    path('ingredients', get_all_ingredients, name='get_all_ingredients'),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
]

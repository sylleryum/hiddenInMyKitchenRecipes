from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class Meal(BaseModel):
    idMeal: str
    strMeal: str
    strDrinkAlternate: Any
    strCategory: str
    strArea: str
    strInstructions: str
    strMealThumb: str
    strTags: Any
    strYoutube: str
    strIngredient1: str
    strIngredient2: str
    strIngredient3: str
    strIngredient4: str
    strIngredient5: str
    strIngredient6: str
    strIngredient7: str
    strIngredient8: str
    strIngredient9: str
    strIngredient10: str
    strIngredient11: str
    strIngredient12: str
    strIngredient13: str
    strIngredient14: str
    strIngredient15: str
    strIngredient16: Any
    strIngredient17: Any
    strIngredient18: Any
    strIngredient19: Any
    strIngredient20: Any
    strMeasure1: str
    strMeasure2: str
    strMeasure3: str
    strMeasure4: str
    strMeasure5: str
    strMeasure6: str
    strMeasure7: str
    strMeasure8: str
    strMeasure9: str
    strMeasure10: str
    strMeasure11: str
    strMeasure12: str
    strMeasure13: str
    strMeasure14: str
    strMeasure15: str
    strMeasure16: Any
    strMeasure17: Any
    strMeasure18: Any
    strMeasure19: Any
    strMeasure20: Any
    strSource: Any
    strImageSource: Any
    strCreativeCommonsConfirmed: Any
    dateModified: Any


class Model(BaseModel):
    meals: List[Meal]

from typing import Any, Self, Optional
import pandas as pd
import os
import json
from dataclasses import dataclass, field
from src.macros import Macros

@dataclass
class Food:
    #cal, carbs, fats, proteins
    name: str = field(default_factory=str)
    """macros per 100g"""
    macros: Macros = field(default_factory=Macros)
    unit: str = field(default_factory=str)


    def __str__(self) -> str:
        return (f'{self.name}:\n'
                f'{self.macros.calories} kcal/100g,\n'
                f'{self.macros.carbs} carbs/100g,\n'
                f'{self.macros.fats} fats/100g,\n'
                f'{self.macros.proteins} proteins/100g')

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "calories": self.macros.calories,
            "carbs": self.macros.carbs,
            "fats": self.macros.fats,
            "proteins": self.macros.proteins,
        }

    @classmethod
    def from_dict(cls, d: dict) -> Self:
        return cls(d["name"], Macros(d["cals"], d["carbs"], d["fats"], d["proteins"]), d['portion'])

    @classmethod
    def load_foods(cls, source) -> list[Self]:
        if os.path.exists(source):
            with open(source, 'r') as f:
                foods = json.load(f)
                return [cls.from_dict(food) for food in foods]
        return []

    @classmethod
    def load_foods_csv(cls, source):
        foods = pd.read_csv(source)
        food_dict = foods.to_dict("records")
        return [cls.from_dict(food) for food in food_dict]

    @staticmethod
    def save_foods(target: str, foods: list["Food"]) -> None:
        with open(target, 'w') as f:
            json.dump([food.to_dict() for food in foods], f, indent=4)

    @classmethod
    def find_food(cls, food_list: list[Self], food_to_find: str) -> Optional[Self]:
        iterator = (food for food in food_list if food.name == food_to_find)
        return next(iterator, None)

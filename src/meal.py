from dataclasses import dataclass, field
from src.food import Food
from src.macros import Macros

@dataclass
class Meal:
    # amount always in grams
    # items = [(food, amount),(food, amount),(food, amount)]
    items: list[tuple[Food, float]] = field(default_factory=list)

    def get_macros(self) -> list[tuple[str, Macros]]:
        return [
                (
                    food.name, food.macros.scale(amount)
                 )
                for food, amount in self.items
            ]

    def get_total_macros(self) -> Macros:
        total_macros = sum((macros for _, macros in self.get_macros()), start=Macros())
        return total_macros

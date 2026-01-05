from dataclasses import dataclass, field
from typing import Self

@dataclass
class Macros:
    calories: float = field(default_factory=float)
    carbs: float = field(default_factory=float)
    fats: float = field(default_factory=float)
    proteins: float = field(default_factory=float)

    def __str__(self):
        return (
                f"Calories: {self.calories} kcal, "
                f"Carbs: {self.carbs} g, "
                f"Fats: {self.fats} g, "
                f"Proteins: {self.proteins} g"
        )
    def scale(self, factor: float) -> "Macros":
        # factor = amount / 100.0
        return Macros(
            calories=self.calories * factor,
            carbs=self.carbs * factor,
            fats=self.fats * factor,
            proteins=self.proteins * factor,
        )

    def __add__(self, other: Self | None) -> "Macros":
        """Soma macros de duas instâncias."""
        if other is None:
            return self

        return Macros(
            calories=self.calories + other.calories,
            carbs=self.carbs + other.carbs,
            fats=self.fats + other.fats,
            proteins=self.proteins + other.proteins,
        )

import os

from pathlib import Path
from fzf_wrapper import prompt
from pandas import melt

# raiz do projeto = dois níveis acima deste arquivo (src/calories_tracker/ -> projeto/)
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
FOOD_FILE = DATA_DIR / "parsed_food.csv"

from src.food import Food
from src.meal import Meal
from src.macros import Macros


#cal, carbs, fats, proteins
class CaloriesTracker:
    def __init__(self) -> None:
        self.meals = list()
        self.foods = Food.load_foods_csv(FOOD_FILE)
        self.choices = {
            "1": self.add_meal,
            "2": self.summarize,
            # "3": self.add_food,
            # "4": self.list_foods,
        }

    def run_program(self) -> None:
        while True:
            self.print_menu()
            choice = input("Please enter your choice: ")
            self.parse_choices(choice)

    @staticmethod
    def print_menu() -> None:
        # os.system("clear")
        print("\nWelcome to the calories calculator\n")
        print("\n----------------------\n")
        print("(1) - Add meal")
        print("(2) - View current calories and macros")
        # print("(3) - Add new food")
        print("(q) - Exit")
        print("\n----------------------\n")

    def add_meal(self) -> None:
        os.system("clear")
        print("Adding meal")
        meal = Meal()

        while True:
            print("what have you eaten?")
            food_names = [food.name for food in self.foods]
            # print(food_names)
            try:
                food_name = prompt(food_names , '--multi')[0]
                food = Food.find_food(self.foods, food_name)
            except IndexError:
                self.invalid_choice()
                continue

            try:
                amount = float(input(f"how much {food.unit} of {food.name} have you eaten?"))
            except ValueError:
                self.invalid_choice()
                continue

            meal.items.append((food, amount))

            if input("Do you want to add more to your meal? (y/n): ").lower() == "n":
                break

        self.meals.append(meal)
        print("meal added")

    # def add_food(self) -> None:
    #     os.system("clear")
    #     print("Adding food")
    #
    #     while True:
    #         new_food = Food()
    #         food_name = input("what food would you like to add to the database?").lower()
    #         if Food.find_food(self.foods, food_name):
    #             print("food already registered")
    #             continue
    #
    #         new_food.name = food_name
    #
    #         while True:
    #             try:
    #                 values = input(
    #                     "Enter macros per 100g (kcal carbs fats proteins): "
    #                 ).split()
    #                 if len(values) != 4:
    #                     raise ValueError("Please enter exactly 4 numbers.")
    #
    #                 food_macros = tuple(map(float, values))
    #                 new_food.macros = Macros(*food_macros)
    #                 break
    #             except ValueError as e:
    #                 print(f"Invalid input: {e}")
    #
    #         self.foods.append(new_food)
    #         if input("Do you want to add a new food? (y/n): ").lower() == "n":
    #             break
    #
    #     Food.save_foods(FOOD_FILE, self.foods)

    # def list_foods(self) -> None:
    #     os.system("clear")
    #     print("Available foods:")
    #     for food in self.foods:
    #         print(food.name)
    #     input("Press enter to continue...")

    def summarize(self) -> None:
        os.system("clear")
        if len(self.meals) == 0:
            print("No meals registered")

        total_macros = sum((meal.get_total_macros() for meal in self.meals), Macros())
        print(total_macros)
        print()
        print("---------------\n")
        # print(f"you have eaten {meal.items for meal in self.meals if self.meals else "nothing"}")
        for meal in self.meals:
            for item in meal.items:
                # print(item)
                print(f"{item[0].name}: {item[1]}")
        print("Press Enter to continue...")
        input()



    @staticmethod
    def invalid_choice() -> None:
        print("Invalid choice. Please try again.")

    def parse_choices(self, choice: str) -> None:
        if choice == "q":
            exit()
        else:
            action = self.choices.get(choice, self.invalid_choice)
            action()

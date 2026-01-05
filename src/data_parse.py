import os
import pandas as pd
import json
import pprint

HOME_DIR = os.environ.get("HOME")
PROJECT_DIR = "Documents/unileipzig/01-inf/code/calories_tracker"
DATA_DIR = os.path.join(HOME_DIR, PROJECT_DIR, 'data')

file_name = "food_json_2025-04-24-original.json"
file_path = os.path.join(DATA_DIR, file_name)

csv_file = "parsed_food.csv"
csv_path = os.path.join(DATA_DIR, csv_file)

with open(file_path) as file:
    full_data = json.load(file)['FoundationFoods']

parsed_data = list()
for item in full_data:
    name = item.get('description')
    category = item.get("foodCategory").get("description")
    portion = item.get("foodPortions", None)

    if portion:
        # print(item['foodPortions'][0]['measureUnit']["name"])
        portion = item.get('foodPortions')[0]["measureUnit"]["name"]

    parsed_item = {
        "name": name,
        "category": category,
        "protion": portion,
        "carbs": None,
        "proteins": None,
        "fats": None,
    }

    for nutrient in item.get("foodNutrients"):
        n_name = nutrient['nutrient']['name']
        n_amount = nutrient.get('amount')

        if n_name == 'Energy':
            parsed_item["cals"] = n_amount

        if n_name == 'Carbohydrate, by difference':
            parsed_item["carbs"] = n_amount

        if n_name == 'Protein':
            parsed_item["proteins"] = n_amount
             
        if n_name == 'Total lipid (fat)':
            parsed_item["fats"] = n_amount

    parsed_data.append(parsed_item)

if "__main__" == __name__:
    df = pd.DataFrame(parsed_data)
    df.to_csv(csv_path, index=False)

    # pprint.pprint(parsed_data[0:10])

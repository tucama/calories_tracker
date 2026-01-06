# Project for the module "Einführung in die Informatik" at Universität Leipzig
# Hackaton 2025

Students:
Arthur Araújo de Lacerda,

Leonhard Karl Scheuernstuhl

## Calories Tracker

This python app was developed during a Hackaton conducted by prof Wiesenecker

The app utilizes a food data based from FDA in order to gather nutrient information of each food
and allow to calculate the intake of proteins, lipids, carbohydrates and calories by the user

## How to use the app

### 0 - Instalation
```bash
# intialize venv and install dependencies
$ . .venv/bin/activate
$ pip install fzf_wrapper pandas

# run the porgrammg
$ python3 kkal/app.py
```

Once called the program a menu shows up with 3 options

### 1 - insert a meal
Chose foods from data base and amount of intake to add them to the calculation

### 2 - summarize
Show macronutrient intake based on meals added

### q - quit
quits

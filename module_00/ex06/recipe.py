# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plouvel <plouvel@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/07 18:42:30 by plouvel           #+#    #+#              #
#    Updated: 2023/03/07 18:46:05 by plouvel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import exit

cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": "10",
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": "60",
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": "15",
    },
}


def printRecipe(name):
    recipe = cookbook.get(name, None)
    if recipe == None:
        return recipe
    print(
        f"""Recipe for {name}
    Ingredients list: {recipe['ingredients']}
    To be eaten for {recipe['meal']}.
    Takes {recipe['prep_time']} minutes of cooking."""
    )
    return recipe


def printRecipes():
    for recipe in cookbook:
        printRecipe(recipe)


def deleteRecipe(name):
    return cookbook.pop(name, None)


def addRecipe(name, ingredients, meal_type, prep_time):
    cookbook[name] = {
        "ingredients": ingredients,
        "meal": meal_type,
        "prep_time": prep_time,
    }


def printOptions():
    print(
        """List of available option:
\t1: Add a recipe
\t2: Delete a recipe
\t3: Print a recipe
\t4: Print the cookbook
\t5: Quit\n"""
    )


def interactiveAddRecipe():
    name = input(">>> Enter a name:\n")
    if name == "":
        return
    print(">>> Enter ingredients:")
    ingredients = []
    while True:
        ingredient = input()
        if ingredient == "":
            break
        else:
            ingredients.append(ingredient)
    meal_type = input(">>> Enter a meal type:\n")
    if meal_type == "":
        return
    prep_time = ""
    while True:
        prep_time = input(">>> Enter a preparation time:\n")
        if prep_time.isdigit():
            break
        else:
            print("Preparation time must be a non negative integer")
    addRecipe(name, ingredients, meal_type, prep_time)
    print("Recipe added !")


def interactiveDeleteRecipe():
    while True:
        name = input(">>> Enter a recipe name:\n")
        if name == "":
            break
        if deleteRecipe(name) != None:
            print("Recipe deleted!")
            break
        else:
            print("Invalid recipe name.")


def interactivePrintRecipe():
    while True:
        name = input(">>> Enter a recipe name:\n")
        if name == "":
            break
        if printRecipe(name) != None:
            break
        else:
            print("Invalid recipe name.")


action = {
    "1": interactiveAddRecipe,
    "2": interactiveDeleteRecipe,
    "3": interactivePrintRecipe,
    "4": printRecipes,
    "5": exit,
}

if __name__ == "__main__":
    print("Welcome to the Python Cookbook!")
    printOptions()
    while True:
        user_input = input("Please select an option:\n>> ")
        fn = action.get(user_input, None)
        if fn == None:
            print("Sorry, this option does not exist.")
            printOptions()
        else:
            fn()

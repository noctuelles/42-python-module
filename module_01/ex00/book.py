# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plouvel <plouvel@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/08 11:17:01 by plouvel           #+#    #+#              #
#    Updated: 2023/03/08 15:29:56 by plouvel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime
from recipe import Recipe


class Book:
    def __init__(self, name) -> None:
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not name:
            raise ValueError("name cannot be empty")
        self.creation_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.last_update = self.creation_date
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}

    def get_recipe_by_name(self, name) -> Recipe:
        """Prints a recipe with the name \texttt{name} and returns the instance"""

        for key in self.recipes_list:
            for recipe in self.recipes_list[key]:
                if recipe.name == name:
                    return recipe
        raise ValueError(f"recipe {name} doesn't exist")

    def get_recipes_by_types(self, recipe_type) -> list:
        """Get all recipe names for a given recipe_type"""

        if not isinstance(recipe_type, str):
            raise TypeError("recipe_type must be a string")
        recipes = self.recipes_list.get(recipe_type, None)
        if recipes == None:
            raise ValueError("recipe_type must be either starter, lunch or dessert")
        return [recipe.name for recipe in recipes]

    def add_recipe(self, recipe) -> None:
        """Add a recipe to the book and update last_update"""

        if not isinstance(recipe, Recipe):
            raise TypeError("recipe must be an instance of Recipe class")
        if recipe.name in [r.name for r in self.recipes_list[recipe.recipe_type]]:
            raise ValueError(f"recipe {recipe.name} already exist in that recipe type")
        self.last_update = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.recipes_list[recipe.recipe_type].append(recipe)


if __name__ == "__main__":
    b = Book("Awesome book")
    b.add_recipe(
        Recipe(
            "caca", 3, 60, ["foods"], "This is the result of human ingestion.", "lunch"
        )
    )
    b.add_recipe(
        Recipe(
            "caca",
            3,
            60,
            ["foods"],
            "This is the result of human ingestion.",
            "starter",
        )
    )
    print(b.get_recipes_by_types("lunch"))

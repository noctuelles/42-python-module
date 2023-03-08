# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plouvel <plouvel@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/08 11:19:20 by plouvel           #+#    #+#              #
#    Updated: 2023/03/08 14:48:58 by plouvel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class Recipe:
    def __init__(
        self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type
    ) -> None:
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not name:
            raise ValueError("name cannot be empty")

        if not isinstance(cooking_lvl, int):
            raise TypeError("cooking_lvl must be an integer")
        if cooking_lvl not in range(1, 6):
            raise ValueError("cooking_lvl must be in range 1-5 included")

        if not isinstance(cooking_time, int):
            raise TypeError("cooking_time must be an integer")
        if cooking_time < 1:
            raise ValueError("cooking_time must be a postive integer")

        if not isinstance(ingredients, list):
            raise TypeError("ingredients must be a list")
        if not ingredients:
            raise ValueError("ingredients cannot be empty")
        for ingredient in ingredients:
            if not isinstance(ingredient, str):
                raise TypeError("each ingredient must be a string")

        if not isinstance(recipe_type, str):
            raise TypeError("recipe_type must be a string")
        if recipe_type not in ("starter", "lunch", "dessert"):
            raise ValueError("recipe_type must be either start, lunch, or dessert")

        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        return f"""\t\t-- Recipe for {self.name} --

\tLevel of difficulty : {self.cooking_lvl}
\tIngredients : {self.ingredients}
\tCooking Time : {self.cooking_time}
\tRecipe type : {self.recipe_type}
\tDescription : {self.description}"""


if __name__ == "__main__":
    r = Recipe(
        "caca", 3, 60, ["foods"], "This is the result of human ingestion.", "lunch"
    )
    print(str(r))

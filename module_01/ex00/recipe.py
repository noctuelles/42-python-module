# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plouvel <plouvel@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/08 11:19:20 by plouvel           #+#    #+#              #
#    Updated: 2023/03/08 13:09:52 by plouvel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class Recipe:
    def __init__(
        self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type
    ) -> None:
        if not isinstance(name, str):
            raise TypeError("name must be a string.")
        if not name:
            raise ValueError("name cannot be empty")

        if not isinstance(cooking_lvl, int):
            raise TypeError("cooking_lvl must be an integer.")
        if cooking_lvl not in range(1, 6):
            raise ValueError("cooking_lvl must be in range 1-5 included.")

        if cooking_time < 1:
            raise ValueError("cooking_time must be a postive integer")
        if recipe_type not in ("starter", "lunch", "dessert"):
            raise ValueError("recipe_type must be either start, lunch, or dessert.")


if __name__ == "__main__":
    r = Recipe("caca", 2, 2, 2, 2, "startesr")

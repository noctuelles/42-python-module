# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plouvel <plouvel@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/06 17:21:25 by plouvel           #+#    #+#              #
#    Updated: 2023/03/06 17:44:50 by plouvel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random import randint

if __name__ == "__main__":
    nbr_to_guess = randint(2, 98)
    attempts = 0
    print(
        """This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!\n"""
    )
    print(nbr_to_guess)
    while True:
        print("What's your guess between 1 and 99?")
        usr_input = input(">> ")
        try:
            if usr_input == "exit":
                print("Goodbye!")
                break
            nbr = int(usr_input)
            attempts += 1
            if nbr < 2 or nbr > 98:
                raise OverflowError
            if nbr < nbr_to_guess:
                print("Too low!")
            elif nbr > nbr_to_guess:
                print("Too high!")
            else:
                if nbr_to_guess == 42:
                    print(
                        "The answer to the ultimate question of life, the universe and everything is 42."
                    )
                print(
                    f"Congratulations{'! You got it on your first try!' if attempts == 1 else ', you got it!'}"
                )
                if attempts != 1:
                    print(f"You won in {attempts} attemps!")
                break
        except ValueError:
            print("That's not a number.")
        except OverflowError:
            print("That's not a correct number.")

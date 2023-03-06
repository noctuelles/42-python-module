# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plouvel <plouvel@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/06 17:18:27 by plouvel           #+#    #+#              #
#    Updated: 2023/03/06 17:18:27 by plouvel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string
import sys


def usage():
    print(
        f"""Translate program arguments string into morse code separated by space.
Usage: {sys.argv[0]} <word1> (word2)..."""
    )
    sys.exit(1)


if __name__ == "__main__":
    AUTH_CHAR = string.ascii_letters + string.digits + " "
    MORSE_DICT = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
        " ": "/",
    }

    args = sys.argv[1:]
    for arg in args:
        if sum(1 for x in arg if x not in AUTH_CHAR):
            print("Error: an argument can only contains alphanumerics and space.")
            sys.exit(1)

    morse_words = ["".join(MORSE_DICT[char.upper()] for char in arg) for arg in args]
    print(*morse_words, sep=MORSE_DICT[" "]) if len(morse_words) else usage()

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plouvel <plouvel@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/06 17:11:08 by plouvel           #+#    #+#              #
#    Updated: 2023/03/06 17:11:37 by plouvel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = {
    "Python": "Guido van Rossum",
    "Ruby": "Yukihiro Matsumoto",
    "PHP": "Rasmus Lerdorf",
}

if __name__ == "__main__":
    for key, value in kata.items():
        print("{0} was created by {1}".format(key, value))

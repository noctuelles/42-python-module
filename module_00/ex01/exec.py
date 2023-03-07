# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plouvel <plouvel@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/07 19:06:23 by plouvel           #+#    #+#              #
#    Updated: 2023/03/07 19:06:24 by plouvel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def main(argc, argv):
    for i, arg in enumerate(reversed(argv[1:])):
        reversed_arg = arg[::-1]
        first_arg_i = argc - 2
        print(
            "".join(c.upper() if c.islower() else c.lower() for c in reversed_arg),
            end=" " if i != first_arg_i else "\n",
        )


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plouvel <plouvel@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/06 17:10:37 by plouvel           #+#    #+#              #
#    Updated: 2023/03/06 17:10:46 by plouvel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import operator


# Wrapper
def math_op(opr1, opr2, op):
    try:
        return str(op(opr1, opr2))
    except ArithmeticError as e:
        return f"ERROR ({e})"


ops = {
    "Sum": lambda a, b: math_op(a, b, operator.add),
    "Difference": lambda a, b: math_op(a, b, operator.sub),
    "Product": lambda a, b: math_op(a, b, operator.mul),
    "Quotient": lambda a, b: math_op(a, b, operator.floordiv),
    "Remainder": lambda a, b: math_op(a, b, operator.mod),
}

if __name__ == "__main__":
    args = sys.argv[1:]
    sys.tracebacklimit = 0
    assert len(args) == 2, "invalid number of arguments."
    for arg in args:
        assert (
            arg[1:].isdigit() if arg[0] == "-" else arg.isdigit()
        ), f"'{arg}' is not an integer."

    a = int(args[0])
    b = int(args[1])
    for key, value in ops.items():
        print(f"{key.ljust(10)} : {value(a, b).rjust(30)}")

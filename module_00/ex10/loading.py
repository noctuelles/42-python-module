# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: plouvel <plouvel@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/06 17:49:59 by plouvel           #+#    #+#              #
#    Updated: 2023/03/07 18:11:25 by plouvel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from time import time


def ft_progress(list):
    list_size = len(list)
    start = time()
    last = 0
    for index, elem in enumerate(list):
        percentage = int(index / list_size * 100)
        progress_bar = "=" + "=" * int(((index / list_size) * 19)) + ">"
        now = time()
        elapsed_time = round(now - start, 2)
        if last != 0:
            eta = str(round(now - last, 2) * (list_size - index)) + "s"
        else:
            eta = "....."
        sys.stdout.write(
            f"ETA: {eta:5} [{percentage:3}%][{progress_bar:21}] {index}/{list_size} | elapsed time {elapsed_time}s\n"
        )
        sys.stdout.flush()
        last = time()
        yield elem

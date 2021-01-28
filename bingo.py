# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 17:31:35 2021

@author: pnp
"""

from random import randint
import time


for draw in range(90):
    drawn_numbers =list()
    bingo_draw=randint(1,90)
    if not bingo_draw in drawn_numbers:
        print(bingo_draw)
        drawn_numbers.append(bingo_draw)
        time.sleep(5)
        pause = input()
        
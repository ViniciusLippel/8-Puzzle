# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:45:20 2021

@author: Vinícius Lippel
"""

import numpy as np
import state


#print puzzle in 2D
def print_puz (pos):
    for i in pos:
        print(i)


#puzzle8 = np.random.choice(9, size=(3,3), replace=False)

puzzle8 = [[3, 2, 4],
           [5, 0, 1],
           [7, 6, 8]]

empty_pos = [1, 1]

state = state.state(puzzle8, empty_pos, 0)

print_puz(state.pos)
print()

state.left()
print_puz(state.pos)
print()

state.up()
print_puz(state.pos)
print()

state.right()
print_puz(state.pos)
print()

state.down()
print_puz(state.pos)
print()



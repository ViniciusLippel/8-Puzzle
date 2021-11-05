# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:45:20 2021

@author: Vinícius Lippel
"""

from treelib import bfs, astar
import state



#print puzzle in 2D
def print_puz (pos):
    for i in pos:
        print(i)


#puzzle8 = np.random.choice(9, size=(3,3), replace=False)

ini_pos = [[3, 2, 4],
           [5, 1, 0],
           [7, 6, 8]]

ini_state = state.state(ini_pos, [1, 2])

goal = [[3, 2, 4],
        [7, 0, 1],
        [6, 5, 8]]


test = bfs(ini_state)
print(test.pos, test.path)
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:45:20 2021

@author: Vinícius Lippel
"""

from solver import bfs, astar
import state

#Initial state positions
ini_pos = [[3, 2, 4],
           [5, 1, 0],
           [7, 6, 8]]

#Goal positions
goal = [[3, 2, 4],
        [7, 0, 1],
        [6, 5, 8]]

#Initial state
ini_state = state.state(ini_pos, [1, 2])


print("\nBFS:\n")
bfs_test = bfs(ini_state, goal)
print("\nFinal state: ", bfs_test.pos, "\nPath:", bfs_test.path)

print("\nA*:")
astar_test = astar(ini_state, goal)
print("\nFinal state: ", astar_test.pos, "\nPath:", astar_test.path)
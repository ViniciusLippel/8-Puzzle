# -*- coding: utf-8 -*-

from solver import bfs, astar
import state

#Initial state positions
ini_pos = [[8, 1, 2],
           [0, 4, 3],
           [7, 6, 5]]

#Goal positions
goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

#Initial state
ini_state = state.state(ini_pos)


print("\nBFS:")
bfs_test = bfs(ini_state, goal)
print("\nFinal state: ", bfs_test.pos, "\nPath:", bfs_test.path)

print("\nA*:")
astar_test = astar(ini_state, goal)
print("\nFinal state: ", astar_test.pos, "\nPath:", astar_test.path)
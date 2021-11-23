# -*- coding: utf-8 -*-

from solver import bfs, astar
import state
import time


#Initial state positions
ini_pos = [[1, 8, 2],
           [0, 4, 3],
           [7, 6, 5]]

#ini_pos = [[1, 3, 4],
           #[8, 6, 2],
           #[0, 5, 7]]

#Goal positions
goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

#Initial state
ini_state = state.state(ini_pos)


#BFS execution
def run_bfs():
    print("\nBFS:")
    
    start = time.time()
    bfs_test = bfs(ini_state, goal)
    end = time.time()
    
    print("\nFinal state: ", bfs_test[0].pos, "\nPath:", bfs_test[0].path)
    print("Nodes: ", bfs_test[1].size())
    print("Time: %fs" % (end-start))


#A* execution
def run_astar():
    print("\n\nA*:")
    
    start = time.time()
    astar_test = astar(ini_state, goal)
    end = time.time()
    
    print("\nFinal state: ", astar_test[0].pos, "\nPath:", astar_test[0].path)
    print("Nodes: ", astar_test[1].size())
    print("Time: %fs" % (end-start))
    
    
run_bfs()
run_astar()
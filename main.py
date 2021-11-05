# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:45:20 2021

@author: Vinícius Lippel
"""

from treelib import Tree
from collections import deque
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

objective = [[3, 2, 4],
             [7, 0, 1],
             [6, 5, 8]]



# Breadth First Search
# =============================================================================

def bfs(ini_state):
    
    global objective
    
    open = deque()
    closed = []
    tree = Tree()
    
    open.append(ini_state)
    tree.create_node(ini_state, ''.join(ini_state.path))

    while open:
        cur_state = open.popleft()
        closed.append(cur_state.pos)
        print(cur_state.pos)
        
        if cur_state.pos == objective:
            solved = cur_state
            return solved
        
        for i in cur_state.move():
            if i:
                tree.create_node(i, ''.join(i.path), 
                                 parent=''.join(cur_state.path))
                if i.pos not in closed:
                    open.append(i)
    
    return solved

# =============================================================================


# A* Search
# =============================================================================

def astar(ini_state):
    return

# =============================================================================

test = bfs(ini_state)
print(test.pos, test.path)
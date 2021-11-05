# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 10:17:59 2021

@author: vinic
"""

from treelib import Tree
from collections import deque
import PriorityQueue

# Breadth First Search
# =============================================================================

def bfs(ini_state, goal):
    
    openset = deque()
    closed = []
    tree = Tree()
    
    openset.append(ini_state)
    tree.create_node(ini_state, ''.join(ini_state.path))

    while openset:
        cur_state = openset.popleft()
        closed.append(cur_state.pos)
        print(cur_state.pos)
        
        if cur_state.pos == goal:
            return cur_state
        
        for st in cur_state.move():
            if st:
                tree.create_node(st, ''.join(st.path), 
                                 parent=''.join(cur_state.path))
                if st.pos not in closed:
                    openset.append(st)



# A* Search
# =============================================================================

def astar(ini_state):
    
    global goal
    
    openset = PriorityQueue()
    closed = set()
    
    openset.add(ini_state)
    
    while openset:
      cur_state = openset.poll()
      
      if cur_state.pos == goal:
        return cur_state
        
      for st in cur_state.move():
        if st not in closed:
          openset.add(st)
      closed.add(cur_state)


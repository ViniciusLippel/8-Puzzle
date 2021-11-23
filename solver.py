# -*- coding: utf-8 -*-

from treelib import Tree
from collections import deque
import heapdict


#Count the number of inverted tiles
def inv_count(arr):
    #arr = list(chain.from_iterable(pos))
    inv_count = 0
    empty_value = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count


#Check if puzzle is solvable by the number of invertions
def is_solvable(puzzle) :
    inv = inv_count([j for sub in puzzle for j in sub])
    return (inv % 2 == 0)


# Breadth First Search
# =============================================================================

def bfs(ini_state, goal):
    
    if not is_solvable(ini_state.pos):
        print("\npuzzle not solvable")
        return ini_state, Tree()
    
    openset = deque()
    closed = {}
    exp_tree = Tree()
    
    openset.append(ini_state)
    exp_tree.create_node(ini_state, ''.join(ini_state.path))

    while openset:
        cur_state = openset.popleft()

        #print(cur_state.pos)
        
        if cur_state.pos == goal:
            return cur_state, exp_tree
        
        for st in cur_state.move():
            if st:
                exp_tree.create_node(st, ''.join(st.path), 
                                 parent=''.join(cur_state.path))
                
                if st.key() not in closed:
                    openset.append(st)
                    
                closed[cur_state.key()] = cur_state.pos
    


# A* Search
# =============================================================================

def astar(ini_state, goal):
    
    if is_solvable(ini_state.pos) == False:
       print("\npuzzle not solvable")
       return ini_state, Tree()
    
    openset = heapdict.heapdict()
    closed = {}
    exp_tree = Tree()
    
    openset[ini_state] = ini_state.evaluation(goal)
    exp_tree.create_node(ini_state, ''.join(ini_state.path))
    
    while openset:
      cur_state = openset.popitem()[0]

      #print(cur_state.pos)
      
      if cur_state.pos == goal:
          return cur_state, exp_tree
         
      for st in cur_state.move():
          if st:
            exp_tree.create_node(st, ''.join(st.path), 
                                 parent=''.join(cur_state.path))
            
            if st.key() not in closed:
                openset[st] = st.evaluation(goal)
            
            closed[cur_state.key()] = cur_state.pos
    
             



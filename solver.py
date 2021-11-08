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
 
    # Count inversions in given 8 puzzle
    inv = inv_count([j for sub in puzzle for j in sub])
 
    # return true if inversion count is even.
    return (inv % 2 == 0)


# Breadth First Search
# =============================================================================

def bfs(ini_state, goal):
    
    if not is_solvable(ini_state.pos):
        print("\npuzzle not solvable")
        return ini_state
    
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

def astar(ini_state, goal):
    
    if is_solvable(ini_state.pos) == False:
       print("puzzle not solvable")
       return ini_state
    
    openset = heapdict.heapdict()
    closed = {}
    
    openset[ini_state] = ini_state.evaluation(goal)
    
    while openset:
      cur_state = openset.popitem()[0]

      print(cur_state.pos)
      
      if cur_state.pos == goal:
          return cur_state
         
      for st in cur_state.move():
          if st:
            if st.key() not in closed:
                openset[st] = st.evaluation(goal)
          closed[cur_state.key()] = cur_state.pos
             



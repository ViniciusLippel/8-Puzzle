# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 16:53:01 2021

@author: vinic
"""

import copy
import numpy as np
from itertools import chain

class state:
    
    def __init__(self, pos, emp):
        self.pos = pos #positions
        self.emp = emp #position of empty
        self.path = []
    
  
    def left(self):
        s = copy.deepcopy(self)
        
        if s.emp[1] != 0:
            tile = s.pos[s.emp[0]][s.emp[1]-1]
            s.pos[s.emp[0]][s.emp[1]-1] = 0
            s.pos[s.emp[0]][s.emp[1]] = tile
            
            s.emp[1] -= 1
            s.path.append('L')
            
            return s
        
        return None
    
    
    def right(self):
        s = copy.deepcopy(self)
        
        if s.emp[1] != 2:
            tile = s.pos[s.emp[0]][s.emp[1]+1]
            s.pos[s.emp[0]][s.emp[1]+1] = 0
            s.pos[s.emp[0]][s.emp[1]] = tile
            
            s.emp[1] += 1
            s.path.append('R')
            
            return s
        
        return None
    
        
    def up(self):
        s = copy.deepcopy(self)
        
        if s.emp[0] != 0:
            tile = s.pos[s.emp[0]-1][s.emp[1]]
            s.pos[s.emp[0]-1][s.emp[1]] = 0
            s.pos[s.emp[0]][s.emp[1]] = tile
            
            s.emp[0] -= 1
            s.path.append('U')
            
            return s
        
        return None
        
    def down(self):
        s = copy.deepcopy(self)
        
        if s.emp[0] != 2:
            tile = s.pos[s.emp[0]+1][s.emp[1]]
            s.pos[s.emp[0]+1][s.emp[1]] = 0
            s.pos[s.emp[0]][s.emp[1]] = tile
            
            s.emp[0] += 1
            s.path.append('D')
            
            return s
        
        return None
    
    
    def move(self):
        return [self.left(), self.right(), self.up(), self.down()]
    
    
    def evaluation(self, goal):
        heuristic = 0
        goal_flat = list(chain.from_iterable(goal))
        pos_flat = list(chain.from_iterable(self.pos))
        
        for i in pos_flat:
            dist = abs(pos_flat.index(i) - goal_flat.index(i))
            
            i = int(dist/3)
            j = int(dist%3)
            
            heuristic = heuristic + i + j
            
        return heuristic
    
    #print puzzle in 2D
    def print_pos (self):
        for i in self.pos:
            print(i)
        
        
        
        
        
        
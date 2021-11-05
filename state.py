# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 16:53:01 2021

@author: vinic
"""

import copy

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
        
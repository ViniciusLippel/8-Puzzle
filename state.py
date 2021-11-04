# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 16:53:01 2021

@author: vinic
"""

class state:
    
    def __init__(self, pos, emp, path):
        self.pos = pos #positions
        self.emp = emp #position of empty
        self.path = path

    
  
    def left(self):
        s = self
        if s.emp[1] != 0:
            tile = s.pos[s.emp[0]][s.emp[1]-1]
            s.pos[s.emp[0]][s.emp[1]-1] = 0
            s.pos[s.emp[0]][s.emp[1]] = tile
            s.emp[1] -= 1
    
    def right(self):
        s = self
        if s.emp[1] != 2:
            tile = s.pos[s.emp[0]][s.emp[1]+1]
            s.pos[s.emp[0]][s.emp[1]+1] = 0
            s.pos[s.emp[0]][s.emp[1]] = tile
            s.emp[1] += 1
        
    def up(self):
        s = self
        if s.emp[0] != 0:
            tile = s.pos[s.emp[0]-1][s.emp[1]]
            s.pos[s.emp[0]-1][s.emp[1]] = 0
            s.pos[s.emp[0]][s.emp[1]] = tile
            s.emp[0] -= 1
         
        
    def down(self):
        s = self
        if s.emp[0] != 2:
            tile = s.pos[s.emp[0]+1][s.emp[1]]
            s.pos[s.emp[0]+1][s.emp[1]] = 0
            s.pos[s.emp[0]][s.emp[1]] = tile
            s.emp[0] += 1
        
        
        
        
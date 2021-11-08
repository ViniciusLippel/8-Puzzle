# -*- coding: utf-8 -*-

from itertools import chain
import copy

class state:
    
    def __init__(self, pos):
        self.pos = pos #positions
        self.emp = self.index_2d(0) #position of empty
        self.path = []
    
    
    #Moving empty left
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
    
    
    #Moving empty right
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
    
    
    #Moving empty up
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
    
    
    #Moving empty down
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
    
    
    #Moving in all possible directions
    def move(self):
        return [self.left(), self.right(), self.up(), self.down()]
    
# =============================================================================
    
    #Evaluation function to A* priority queue 
    def evaluation(self, goal):
        heuristic = 0
        goal_flat = list(chain.from_iterable(goal))
        pos_flat = list(chain.from_iterable(self.pos))
        
        for i in pos_flat:
            dist = abs(pos_flat.index(i) - goal_flat.index(i))
            
            i = int(dist/3)
            j = int(dist%3)
            
            heuristic = heuristic + i + j
            heuristic = heuristic + len(list(chain.from_iterable(self.path)))
            
        return heuristic
    
    
    #Binary search to optimize list search
    def binary_search(self, el, li, start, end):
        if start > end:
            return False

        mid = (start + end) // 2
        
        if el == li[mid]:
            return True
    
        if el < li[mid]:
            return self.binary_search(el, li, start, mid-1)
        
        else:
            return self.binary_search(el, li, mid+1, end)
    
    
    #Check if self.pos is into certain list
    def isin(self, li):
        test = self.binary_search(self.pos, li, 0, len(li)-1)
        return test
    
    
    #print puzzle in 2D
    def print_pos (self):
        for i in self.pos:
            print(i)
    
    
    #Generate key to dictionary
    def key(self):
        return ''.join(str(i) for i in list(chain.from_iterable(self.pos)))
    
    
    #Return the 2d index of value in self.pos
    def index_2d(self, v):
        for i, x in enumerate(self.pos):
            if v in x:
                return [i, x.index(v)]
        
        
        
        
        
        
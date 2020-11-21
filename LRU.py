# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 20:15:07 2020

@author: Brian
"""





def LRU(pg,cap):
    in_memory = []
    faults = 0
    
    for i in pg:
        if i not in in_memory:
            if len(in_memory) == cap:
                in_memory.remove(in_memory[0])
                in_memory.append(i)
            else:
                in_memory.append(i)
            faults += 1
    print("{}".format(faults)) 




#Run function
processList = [3, 1, 6, 5, 3, 4, 6,  
                8, 7, 1, 0, 5, 4,6,2,3,0,1]    
LRU(processList, 1)  
LRU(processList, 2) 
LRU(processList, 3) 
LRU(processList, 4) 
LRU(processList, 5)  
LRU(processList, 6) 
LRU(processList, 7) 
LRU(processList, 8) 
LRU(processList, 9) 
LRU(processList, 10) 


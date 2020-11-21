# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 20:08:40 2020

@author: Brian
"""
  
        
def FCFS(pages, cap):    
    frames = []
    faults = 0
    for i in range(len(pages)):
        if len(frames) < cap:
            if pages[i] not in frames:
                faults += 1
                frames.append(pages[i])
        else:
            if pages[i] not in frames:
                faults += 1
                frames.remove(frames[0])
                frames.append(pages[i])
    return faults
         
       
def LRU(pg,cap):
    frames = []
    faults = 0
    
    for i in pg:
        if i not in frames:
            if len(frames) == cap:
                frames.remove(frames[0])
                frames.append(i)
            else:
                frames.append(i)
            faults += 1
    return faults

            
     
    
    
    
    
    
# Driver code  
if __name__ == '__main__': 
    pages = [3, 1, 6, 5, 3, 4, 6,  
                8, 7, 1, 0, 5, 4,6,2,3,0,1]  
    n = len(pages)  
    capacity = 3
    
    print(FCFS(pages,capacity))
    print(LRU(pages,capacity))
    

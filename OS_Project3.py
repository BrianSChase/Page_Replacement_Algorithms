# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 20:08:40 2020

@author: Brian
"""

import matplotlib.pyplot as plt

        
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
         
       
def LRU2(pg,cap):
    frames = []
    faults = 0

    
    for i in pg:
        if i not in frames:
            if len(frames) == cap:
                frames.remove(frames[0])
                frames.append(i)
            else:
                frames.append(i)
            faults+= 1
        else:
            frames.remove(frames[0])
            frames.append(i)

       
    return faults

def LRU(pg,cap):
    frames = []
    faults = 0
    indexes = {}
    index = 0
    
    for i in pg:
        indexes[i] = index
        if i not in frames:
            if len(frames) == cap:
                min_val = min(indexes, key=indexes.get)
                frames.remove(min_val)
                del(indexes[min_val])
                frames.append(i)
            else:
                frames.append(i)
            faults+= 1

        index += 1
       
    return faults            
 

    
def optimal(pg, cap):
    frames = []
    faults = 0
    furthest = 0
    pg_index = 0
    fr_index = 0
    distances = {}
    #initialize dictionary containing frame distances to 0
    for i in range(cap):
        distances[i] = 0
        
    for i in pg:
        if i not in frames:
            if len(frames) == cap:
                #find furthest away
                for x in frames:
                 
                    #Find the distance to next mathicn elemennt starting
                    #at position index.
                    if x not in pg[pg_index:]:
                        distances[fr_index] = len(pg)
                    else:
                        distances[fr_index] = pg.index(x,pg_index)
                    fr_index += 1 

                    
                    furthest = max(distances, key=distances.get)  

                frames.remove(frames[furthest])#changes frames 0 to frames furthest
                frames.append(i)#change to replaces frames furthest
                fr_index = 0
            else:
                frames.append(i)

            faults += 1
        pg_index += 1
    return faults
 
    
    
    
    
# Driver code  
if __name__ == '__main__': 
    pages = [3, 1, 6, 5, 3, 4, 6,  
                8, 7, 1, 0, 5, 4,6,2,3,0,1]  
    n = len(pages)  
    capacity = 3
    
    cap_list = []
    fcfs = []
    lru = []
    opt = []
    
    
    print(FCFS(pages,capacity))
    print(LRU(pages,capacity))
    print(optimal(pages,capacity))


    for i in range(10):
        cap_list.append(i+1)
        fcfs.append(FCFS(pages,i+1))
        lru.append(LRU(pages,i+1))
        opt.append(optimal(pages,i+1))
    
plt.plot(fcfs, cap_list, label = "fcfs")
plt.plot(lru, cap_list, label = "lru")
plt.plot(opt, cap_list, label = "opt")
plt.xlabel("Frames")
plt.ylabel("Faults")       
plt.legend()        
plt.show()

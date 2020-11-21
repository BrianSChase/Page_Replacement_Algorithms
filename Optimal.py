# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 19:45:29 2020

@author: Brian
"""




def optimal(pg,cap):
    
    temp_pg = pg
    in_memory = []
    faults = 0
    furthest = 0
    dist = 0
    #index into in_memory for finding furthest
    index = 0
    furthest_index = 0
    pg_index = 0
    
    for i in pg:
        print(i)
        temp_pg.remove(temp_pg[0])
        if i not in in_memory: 
            print(": miss\n")
            faults += 1
            #If in_memory is full
            if len(in_memory) == cap: 
                index = 0
                #loop through all values of in_memory
                for k in in_memory:
                   if k in temp_pg:
                       if pg.index(k) < index:
                         dist = temp_pg.index(k)
                         if dist > furthest:
                            furthest = dist
                            furthest_index = index
                            
                            
                   else:
                        furthest = len(pg)
                        furthest_index = index
                   index+= 1
                in_memory[furthest_index] = i
            else:
                in_memory.append(i)
        #pg.remove(pg[0])
        index += 1
        pg_index+= 1
        print(in_memory)


    print("{}".format(faults)) 








pg = [3, 1, 6, 5, 3, 4, 6,  
                8, 7, 1, 0, 5, 4,6,2,3,0,1] 

fn = 3
optimal(pg,fn)


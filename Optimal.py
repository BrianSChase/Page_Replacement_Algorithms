# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 19:45:29 2020

@author: Brian
"""


"""

from queue import Queue  


#Check for page in frame. arr is the array that starts empty in the
#optimal function
def check_page(var, arr):
    for x in arr:
        if x == var:
            return True
    return False

"""
            




  
# Function to find the frame that will not be used 
# recently in future after given index in pg[0..pn-1] 
#pg[] = reference string passed in main (will hold the 100 random in proj)
#vector fr = the vector that starts empty and holds the pages,
    #I think its variable in size (capacity)
#pn = size of pg / one element of pg, 
#index = will be passed from a loop in the main page function   
      

"""
int predict(int pg[], vector<int>& fr, int pn, int index) 
{ 
    // Store the index of pages which are going 
    // to be used recently in future 
    int res = -1, farthest = index; 
    for (int i = 0; i < fr.size(); i++) { 
        int j; 
        for (j = index; j < pn; j++) { 
            if (fr[i] == pg[j]) { 
                if (j > farthest) { 
                    farthest = j; 
                    res = i; 
                } 
                break; 
            } 
        } 
  
        // If a page is never referenced in future, 
        // return it. 
        if (j == pn) 
            return i; 
    } 
  
    // If all of the frames were not in future, 
    // return any of them, we return 0. Otherwise 
    // we return res. 
    return (res == -1) ? 0 : res; 
} 
""" 
 
"""   
    
def predict(pg, fr, fn, index):
    res = -1
    farthest = index
    j = index
    i = 0
    for x in fr:
        while j < len(pg):
            if x == pg[j]:
                if j > farthest:
                    farthest = j
                    res = i
                break
            j+= 1
            i+= 1
            
    if j == len(pg):
        return i
    
    #Not sure if this is right
    if res == 1:
        return 0
    else:
        return res
        
"""

"""
#If page is not in frame
#index variable is the index currently in pg
def future(pg,fr,fn,index):
    farthest = 0
    for x in fr:
        while index < fn:
            if x == pg[index]:
                
            
            
"""           
            
            
    
    
"""
    
void optimalPage(int pg[], int pn, int fn) 
{ 
    // Create an array for given number of 
    // frames and initialize it as empty. 
    vector<int> fr; 
  
    // Traverse through page reference array 
    // and check for miss and hit. 
    int hit = 0; 
    for (int i = 0; i < pn; i++) { 
  
        // Page found in a frame : HIT 
        if (search(pg[i], fr)) { 
            hit++; 
            continue; 
        } 
  
        // Page not found in a frame : MISS 
  
        // If there is space available in frames. 
        if (fr.size() < fn) 
            fr.push_back(pg[i]); 
  
        // Find the page to be replaced. 
        else { 
            int j = predict(pg, fr, pn, i + 1); 
            fr[j] = pg[i]; 
        } 
    } 
    cout << "No. of hits = " << hit << endl; 
    cout << "No. of misses = " << pn - hit << endl; 
} 
"""

"""
        
def optimal(pg, fn):
    # frames = Queue(maxsize = fn)
     frames = []
     hit = 0
     i = 0
     for x in pg:
         for z in frames:    
            if x == z:
                hit += 1
        
         if len(frames) < fn:
            frames.append(pg[i])
         else:
             prediction = predict(pg, frames,fn, i + 1)
             frames[prediction] = pg[i]    
         i += 1    
"""        
"""  
// Driver Function 
int main() 
{ 
    int pg[] = { 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2 }; 
    int pn = sizeof(pg) / sizeof(pg[0]); 
    int fn = 4; 
    optimalPage(pg, pn, fn); 
    return 0; 
} 
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


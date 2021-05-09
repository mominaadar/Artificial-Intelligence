import itertools
import random
from math import exp


g = [[10, 3,  4,   6,  23],
     [9,  32, 12,  2,  34],
     [7,  8,  100, 21, 11],
     [18, 67, 55,  89, 90],
     [22, 33, 14,  44, 110]]
     
     
def schedule(t):
    return (pow(10,7)-t)
     
     
def simulated_annealing(grid, schedule):
    r, c = 2, 2
    current = [r,c]
    current_val = grid[current[0]][current[1]]

    
    found = False
    prob = 0
    
    # loop will run infinitely
    for t in itertools.count():
        if t == 0:
            continue
        
        probs = []
        max_prob = 0

        T = schedule(t)
#         print('Value of T:',T)
        
        if T == 0:
            return (r,c)
        
        
        neighbors = []
        
        up = [r-1, c]
        dwn = [r+1, c]
        rgt = [r, c+1]
        lft = [r, c-1]
        
        if up[0] >= 0 and up[0] <= 4 and up[1] >= 0 and up[1] <= 4:
#             print('up',up)
            neighbors.append(['up',up])
        
        if dwn[0] >= 0 and dwn[0] <= 4 and dwn[1] >= 0 and dwn[1] <= 4:
#             print('dwn',dwn)
            neighbors.append(['dwn',dwn])
            
        if rgt[0] >= 0 and rgt[0] <= 4 and rgt[1] >= 0 and rgt[1] <= 4:
#             print('rgt',rgt)
            neighbors.append(['rgt',rgt])
        
        if lft[0] >= 0 and lft[0] <= 4 and lft[1] >= 0 and lft[1] <= 4:
#             print('lft',lft)
            neighbors.append(['lft',lft])
            
        x = random.choice(neighbors)
#         print('Randomly chosen:',x)
        a, b = x[1][0], x[1][1]
        
        next_ = [a,b]
        next_val = grid[next_[0]][next_[1]]
        
        delta_E = next_val - current_val
#         print(next_val, current_val)
#         print('Delta E val:',delta_E)
        
        if delta_E > 0:
            current = next_
            r, c = next_[0], next_[1]
            current_val = grid[current[0]][current[1]]
#             print('New current when E > 0',current)
            
        else:
            #check for all neighbors
            for n in neighbors:
                if n[1] == current:
                    continue
                else:
#                     print('Neighbors:',n)
                    a, b = n[1][0], n[1][1]
                    delta_E = grid[a][b] - grid[current[0]][current[1]]
                    e = exp(delta_E/T)
#                     print('Probability (e)',e)

                    probs.append([[a,b], e])
            
            for p in probs:
                if p[1] > max_prob:
                    max_prob = p[1]
                    r, c = p[0][0], p[0][1]
            
#             print('Maximum probability:',max_prob,'State:',r,',',c)
            current = [r, c]
            current_val = grid[current[0]][current[1]]

#             print('New current:',current)
#             print('-----------------')


if __name__ == '__main__':

    state = simulated_annealing(g, schedule)
    print(state)
                
                
            
            

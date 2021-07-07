import itertools
import random
from math import exp


board = [['Z','A','E','B','W','$'],
         ['H','F','G','X','F','D'],
         ['*','R','S','#','M','K'],
         ['G','H','T','O','R','L'],
         ['D','I','@','S','C','Y'],
         ['V','W','N','P','Q','X']]
 
 
def schedule(t):
    return (pow(10,7)-t)        
         
# -------------------------------------------------------------------

def simulated_annealing(grid, schedule):
    r, c = 0,0
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
        
        if T == 0:
            return (r,c)
        
        
        neighbors = []
        
        up = [r-1, c]
        dwn = [r+1, c]
        rgt = [r, c+1]
        lft = [r, c-1]
        
        if up[0] >= 0 and up[0] <= 5 and up[1] >= 0 and up[1] <= 5:
            neighbors.append(['up',up])
        
        if dwn[0] >= 0 and dwn[0] <= 5 and dwn[1] >= 0 and dwn[1] <= 5:
            neighbors.append(['dwn',dwn])
            
        if rgt[0] >= 0 and rgt[0] <= 5 and rgt[1] >= 0 and rgt[1] <= 5:
            neighbors.append(['rgt',rgt])
        
        if lft[0] >= 0 and lft[0] <= 5 and lft[1] >= 0 and lft[1] <= 5:
            neighbors.append(['lft',lft])
            
        x = random.choice(neighbors)
        a, b = x[1][0], x[1][1]
        
        next_ = [a,b]
        next_val = grid[next_[0]][next_[1]]
        
        delta_E = ord(next_val) - ord(current_val)
        
        if delta_E > 0:
            current = next_
            r, c = next_[0], next_[1]
            current_val = grid[current[0]][current[1]]
            
        else:
            #check for all neighbors
            for n in neighbors:
                if n[1] == current:
                    continue
                else:
                    a, b = n[1][0], n[1][1]
                    delta_E = ord(grid[a][b]) - ord(grid[current[0]][current[1]])
                    e = exp(delta_E/T)

                    probs.append([[a,b], e])
            
            for p in probs:
                if p[1] > max_prob:
                    max_prob = p[1]
                    r, c = p[0][0], p[0][1]
            
            current = [r, c]
            current_val = grid[current[0]][current[1]]
            
# -------------------------------------------------------------------  

if __name__ == '__main__':

    print('The code is executing, please wait..')
    r, c = simulated_annealing(board, schedule)
    print(r,c)



# ----- Momina Atif Dar - P18-0030 ----------

import random

from datetime import datetime, timedelta

matrix = [[0,60,100,510,620,40,70,80,120,650],
          [60,0,60,130,40,80,90,90,440,540],
          [100,60,0,450,450,860,910,190,10,145],
          [510,130,450,0,70,1500,440,220,660,250],
          [620,40,450,70,0,260,160,330,120,50],
          [40,80,860,1500,260,0,370,260,350,110],
          [70,90,910,440,160,370,0,50,120,270],
          [80,90,190,220,330,260,50,0,330,990],
          [120,440,10,660,120,350,120,330,0,330],
          [650,540,145,250,50,110,270,990,330,0]]
          
# --------------------------------------------------------------------------------

def initial_population(matrix):
    parents = []
    
    for i in range(10):
        P = []
        for i in range(len(matrix[0])):
            random_int = random.randint(1,10)
            P.append(random_int)
        parents.append(P)  
    
    return parents
    
# ---------------------------------------------------------------------------------    

def selection(parents):
    selected = []
    
    for i in range(int(len(parents)/2)):
        lst = []
        r1 = random.randint(0,len(parents)-1)
        r2 = random.choice([i for i in range(0,len(parents)) if i not in [r1]])
        
        lst.append(parents[r1])
        lst.append(parents[r2])
        
        selected.append(lst)

        
    return selected
    
# ---------------------------------------------------------------------------------
    
def crossover(selected):
    
    children = []
    
    n = len(selected[0][0])
    crossover_pt = random.randint(1,n-1)
    
    for i in range(len(selected)):
        
        P0 = selected[i][0]
        P1 = selected[i][1]
        
        left_P0 = P0[:crossover_pt]
        right_P0 = P0[crossover_pt:]

        left_P1 = P1[:crossover_pt]               
        right_P1 = P1[crossover_pt:]

        child1 = []

        for i in left_P0:
            child1.append(i)
        for i in right_P1:
            child1.append(i)
            
        children.append(child1)
        
        
        child2 = []
    
        for i in left_P1:
            child2.append(i)
        for i in right_P0:
            child2.append(i)
            
        children.append(child2)

    
    for i in children:
        for j in range(len(i)):

            r = random.randint(1,25)
            r2 = [1,2,3,4,5,6,7,8,9,10]

            if r == 15:
                for k in r2:
                    if k not in i:
                        i[j] = k
        
    return children

# ------------------------------------------------------------------------------------

def mutation(children):
    
    r1 = random.randint(0,9)
    r2 = random.choice([i for i in range(0,9) if i not in [r1]])
    
    for i in children:
        temp = i[r1]
        i[r1] = i[r2]
        i[r2] = temp
        
    return children
    
# -------------------------------------------------------------------------------------    
    
def fitness_fn(mutated_children, matrix):
    
    flg = True
    fit_paths = []
    
    # check if all cities visited once 
    
    for i in mutated_children:
        r = [1,2,3,4,5,6,7,8,9,10]
        
        for j in r:
            if j not in i:
                # Child is not fit i.e. Salesperson has not visited all the cities.
                flg = False
        
        if flg == True:
            fit_paths.append(i)
            
            
    # and that path has min cost
    
    if len(fit_paths) > 0:
    
        total_cost = []

        for i in fit_paths:
            cost = 0
            for j in range(len(i)-1):

                dist_from = i[j]
                dist_to = i[j+1]

                cost = matrix[dist_from-1][dist_to-1] + cost

            total_cost.append(cost)
        
        min_cost = float('inf')
        for i in range(len(total_cost)):
            if total_cost[i] < min_cost:
                min_cost = total_cost[i]
                best_path = mutated_children[i]
    
        return best_path, min_cost
    
    return None, None
    
# -----------------------------------------------------------------------------------
    
def genetic_algo(matrix):
    
    end_time = datetime.now() + timedelta(seconds=3)
    
    min_cost = float('inf')
    
    parents = initial_population(matrix)
#     print('Initial population (Parents):',parents)
    
    while datetime.now() < end_time:
        
        small_random_prob = random.uniform(0,1)


        selected = selection(parents)
#         print('Selected parents:',selected)

        children = crossover(selected)
#         print('Children after crossover:',*children,sep='\n')
        
        
        if small_random_prob < 0.5:
            mutated_children = mutation(children)
#             print('Mutated children:',*mutated_children, sep='\n')

            best_path, path_cost = fitness_fn(mutated_children, matrix)

            if best_path and min_cost:
    #             print('path',best_path, 'cost', min_cost)
                if path_cost < min_cost:
                    min_cost = path_cost
                    p = best_path

            else:
                parents = mutated_children    
    
#    print('Best path:',p,' Min cost we got:',min_cost)            
    
    return p, min_cost


# ---------------------------------------------------------------------------------
    
if __name__ == '__main__':

    print('Please wait, the algorithm is running for 3 seconds to choose the optimal path')

    path, min_cost = genetic_algo(matrix)
    print('Path:',path,'Min cost:',min_cost)
    
    
    # ORAL DISCUSSION

# I chose this chromosome representation of len 10 because there are total of 10 cities saleperson has to visit. I have selected cities randomly from 1 to 10 and made chromosomes with duplication.
# I chose 10 parents as initial population so more children can pe produced with more chances of mutation and better results. 
# At every iteration crossover rate is selected randomly to increase efficiency of algorithm.
# Mutation probability is set to 0.5 because I have observed it gives me minimum path of 600 with all the cities visited once only.
# It starts off as just random cities visited and after some iterations more duplications are removed as crossover is done. Random swapping in mutation helps in getting more different paths who may have lesser cost. So, after a certain point (3 seconds) from all the paths explored, the path with the minimum cost comes out as result.

# P.S. I have run algirthm for almost 5000 times and the minimum cost it has given me is 600 for all the cities visited.





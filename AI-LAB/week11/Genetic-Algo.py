
#  ------------ Momina Atif Dar - P18-0030 ---------------

import random


init_state = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
      
      
              
initial_state = []
def get_1D(init_state):
    for i in init_state:
        for j in i:
            initial_state.append(j)
            
    return initial_state
    


def get_population(init_state):
    P = []
    for i in range(1,5):
        X = []
        
        for j in range(0,len(init_state)):
            chromo = random.randint(0,1)
            X.append(chromo)
        P.append(X)
    
    return P
    
    
    
def fitness_fn(population):
    fitness_vals = []
    for i in population:
        count = 0
        for j in i:
            if j == 1:
                count += 1
        fitness_vals.append(count)
    
    return fitness_vals
    
    
    
def random_selection(population, fitness_fn, selected):    
    fitness_vals = fitness_fn(population)
    probs = []
    max_prob = 0
    
    for i in fitness_vals:
        p = i/sum(fitness_vals)
        probs.append(p)
    
    
    for i in range(0,len(probs)):
        if probs[i] > max_prob:
            if i not in selected:
                max_prob = probs[i]
                index = i
    
    selected.append(index)

    return population[index], selected
    
    
    
def reproduce(x, y):
    n = len(x)
    
    # random crossover point
    c = random.randint(1,n)

    print('crossover point:',c)
    
    left_x = x[:c]

    right_y = y[c:]
    
    child = []
    
    print('x:',left_x)
    print('y:',right_y)
    
    for i in left_x:
        child.append(i)
    for i in right_y:
        child.append(i)
    
    print('child:',child)
    return child
            
   
    
def mutate(child):
    
    for i in range(0,len(child)):
        val = random.randint(0,100)
        
        # fixed 25 from 0-100, if 25 comes then mutation takes place
        if val == 25:
            pos = i
            child[i] = 1
    
    return child
    
    
    
def goal_test(population):
    fitness_vals = fitness_fn(population)
    print('Fitness vals:',fitness_vals)
    max_val = 0
    for i in range(0,len(fitness_vals)):
        if fitness_vals[i] > max_val:
            max_val = fitness_vals[i]
            index = i
    
    return population[index]
    
    
    
def genetic_algo(population, fitness_fn):
    
    leave = False
        
    small_random_probability = 0.01
    while True:    #change it afterwards
        new_population = []
        
        # selection
        for i in range(0,len(population)):
            selected = []
            x, selected  = random_selection(population, fitness_fn, selected)
            print('random X:',x)

            y, select  = random_selection(population, fitness_fn, selected)
            print('random Y:',y)

            
                
            # crossover
            child = reproduce(x,y)
            
            # mutation
            if small_random_probability == 0.01:
                child = mutate(child)
                print('Mutated child:',child)
                print('---------------')
            
            new_population.append(child)
        
        population = new_population
        print('New population:',population)
        
        # to break while loop when we get goal state of child (all 1's)
        for i in population:
            count = 0
            for j in i:
                if j == 1:
                    count += 1
            
            print('count:',count)
            if count == len(population[0]):
                leave = True
                break
        
        if leave == True:
            break
    
    # evaluation
    best_individual = goal_test(population)
    return best_individual



if __name__ == '__main__':

    init_state = get_1D(init_state)
    population = get_population(init_state)
    print('population:',population)
    result = genetic_algo(population, fitness_fn)
    print('Best individual:', result)     
            


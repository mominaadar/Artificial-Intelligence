
# PART D

import random

class Environment:
    def __init__(self):
        #instantiate locations and conditions
        # 0.8 indicates Clean and 0.2 indicates Dirty
        
        self.locationCondition = {'A':'0','B':'0','C':'0','D':'0','E':'0','F':'0','G':'0','H':'0','I':'0'}
        self.pathCost = {'A':10,'B':8,'C':12,'D':7,'E':3,'F':2,'G':5,'H':1,'I':9}
        
        #randomize conditions in location A-I
        
        self.locationCondition['A'] = random.choice([0.2,0.8])
        self.locationCondition['B'] = random.choice([0.2,0.8])
        self.locationCondition['C'] = random.choice([0.2,0.8])
        self.locationCondition['D'] = random.choice([0.2,0.8])
        self.locationCondition['E'] = random.choice([0.2,0.8])
        self.locationCondition['F'] = random.choice([0.2,0.8])
        self.locationCondition['G'] = random.choice([0.2,0.8])
        self.locationCondition['H'] = random.choice([0.2,0.8])
        self.locationCondition['I'] = random.choice([0.2,0.8])
    
###############################################################   
    
def move_clean(Environment):
    
    stk = []

    score = 0
    
    dic = {'A':['right','down'], 'B':['left','right','down'], 'C':['left','down'], 'D':['up','down','right'],
       'E':['up','down','left','right'], 'F':['up','down','left'], 'G':['up','right'], 'H':['up','left','right'],'I':['up','left'] }
    
    visited = []
    
    #assume agent is initially in the middle
    agentLoc = 'E'
    stk.append(agentLoc)
    
    print('Before:',Environment.locationCondition)

    while stk:
        agentLoc = stk.pop(0)
        print('Agent is now in room ',agentLoc)

        if agentLoc not in visited:
            score = clean_room(Environment, dic, score, agentLoc)
            visited.append(agentLoc)
#             print('score',score)
            
            # adding search cost i.e. node visited
            score += 1

            if len(visited) != 9:
                ans = get_direction(dic, agentLoc)
                stk.append(ans)
            
    
    print('After:',Environment.locationCondition)
    print('Score:',score)

########################################################

def clean_room(Environment, dic, score, room):
    
    # decrement for moving to the room except for E because agent is starting from E
    if room != 'E':
        score -= 1
    
    # if room dirty
    if Environment.locationCondition[room] == 0.2:
        print(room,' is dirty')
        
        #suck dirt and mark clean
        Environment.locationCondition[room] = 0.8
        print(room,' has been cleaned')
        
        # adding path cost to performance measure(cleaning room)
        if room != 'E':
            score = score + 1 + Environment.pathCost[room]
        else:
            score = score + 1
            
    elif Environment.locationCondition[room] == 0.8:
        score = score + Environment.pathCost[room]
        print(room,' is already clean')
        
    return score

########################################################

# assuming our agent will go from E -> B -> A -> D -> G -> H -> I -> F -> C

def get_direction(dic, agentLoc):
    if agentLoc == 'E':
        for i in dic.items():
            for j in i[1]:
                if j == 'up':
                    return 'B'
    elif agentLoc == 'B':
        for i in dic.items():
            for j in i[1]:
                if j == 'left':
                    return 'A'
    elif agentLoc == 'A':
        for i in dic.items():
            for j in i[1]:
                if j == 'down':
                    return 'D'
    elif agentLoc == 'D':
        for i in dic.items(): 
            for j in i[1]:
                if j == 'down':
                    return 'G'
    elif agentLoc == 'G':
        for i in dic.items():
            for j in i[1]:
                if j == 'right':
                    return 'H'
    elif agentLoc == 'H':
        for i in dic.items():
            for j in i[1]:
                if j == 'right':
                    return 'I'
    elif agentLoc == 'I':
        for i in dic.items():
            for j in i[1]:
                if j == 'up':
                    return 'F'
    elif agentLoc == 'F':
        for i in dic.items():
            for j in i[1]:
                if j == 'up':
                    return 'C'
    elif agentLoc == 'C':
        return True        

###########################################################3

if __name__ == '__main__':
    
	env = Environment()
	td = move_clean(env)
	
	

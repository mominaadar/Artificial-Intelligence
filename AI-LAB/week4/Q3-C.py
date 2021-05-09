
# PART C 

class Environment:
    def __init__(self):
    
        #instantiate locations and conditions
        # 0 indicates Clean and 1 indicated Dirty
        
        self.locationCondition = {'A':'0','B':'0','C':'0','D':'0','E':'0','F':'0','G':'0','H':'0','I':'0'}
        
        #assuming all rooms are dirty
        self.locationCondition['A'] = 1
        self.locationCondition['B'] = 1
        self.locationCondition['C'] = 1
        self.locationCondition['D'] = 1
        self.locationCondition['E'] = 1
        self.locationCondition['F'] = 1
        self.locationCondition['G'] = 1
        self.locationCondition['H'] = 1
        self.locationCondition['I'] = 1

##############################################################

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

    # visiting all the 9 squares
    while stk:
        agentLoc = stk.pop(0)
        print('Agent is now in room ',agentLoc)
            
        if agentLoc not in visited:
            score = clean_room(Environment, dic, score, agentLoc)
            visited.append(agentLoc)

            
            if len(visited) != 9:
                ans = get_direction(dic, agentLoc)
                stk.append(ans)
            
    
    print('After:',Environment.locationCondition)
    print('Score:',score)

##################################################################

def clean_room(Environment, dic, score, room):
    
    # decrement for moving to the room except for E because agent is starting from E
    if room != 'E':
        score -= 1
    
    #check if room dirty
    if Environment.locationCondition[room] == 1:
        #suck dirt and mark clean
        Environment.locationCondition[room] = 0
        score += 1
        
    return score
        
##################################################################

# assuming out agent will go from E -> B -> A -> D -> G -> H -> I -> F -> C

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
        
####################################################################
    
if __name__ == '__main__':
	env = Environment()
	td = move_clean(env)
	
	
	

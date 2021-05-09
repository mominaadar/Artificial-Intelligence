import random

class Environment:
    def __init__(self):
        #instantiate locations and conditions
        # 0 indicates Clean and 1 indicated Dirty
        self.locationCondition = {'A':'0', 'B':'0', 'C':'0', 'D':'0'}
        
        #randomize conditions in location A, B, C and D
        self.locationCondition['A'] = random.randint(0,1)
        self.locationCondition['B'] = random.randint(0,1)
        self.locationCondition['C'] = random.randint(0,1)
        self.locationCondition['D'] = random.randint(0,1)
        
##########################################################

def roomA(Environment, dic, score, count):

    # if A is dirty
    if Environment.locationCondition['A'] == 1:
        count += 1
        print('Location A is dirty')
        
        # suck dirt and mark it clean
        ans = dic[('A',1)]
        if ans == 'Clean':
            Environment.locationCondition['A'] = 0
            score += 1
            print('Location A has been cleaned')
            
            # move to B
            ans = dic[('A',0)]
            if ans == 'Right':
                score -= 1
                print('Moving to B...')
    
    # if A is clean
    elif Environment.locationCondition['B'] == 0:
        print('Location A is already clean')
        
        # move to B
        ans = dic[('A',0)]
        if ans == 'Right':
            score -= 1
            print('Moving to B...')
        
    return score, count
    
##########################################################    
    
def roomB(Environment, dic, score, count):
    
    # if B is dirty
    if Environment.locationCondition['B'] == 1:
        count += 1
        print('Location B is dirty')

        # suck and mark clean
        ans = dic[('B',1)]
        if ans == 'Clean':
            Environment.locationCondition['B'] = 0
            score += 1
            print('Location B has been cleaned')
            
            ans1 = dic[('B',0)][0]
            ans2 = dic[('B',0)][1]

            # move to C
            if ans1 == 'rotate_right' and ans2 == 'Down':
                score -= 1
                print('Rotating')
                print('Moving to C...')
    
    # if B is clean
    elif Environment.locationCondition['B'] == 0:
        print('Location B is already clean')
        
        ans1 = dic[('B',0)][0]
        ans2 = dic[('B',0)][1]
        
        # move to C
        if ans1 == 'rotate_right' and ans2 == 'Down':
            score -= 1
            print('Rotating')
            print('Moving to C...')
            
    
    return score, count
    
##########################################################    
    
def roomC(Environment, dic, score, count):
    
    # if C is dirty
    if Environment.locationCondition['C'] == 1:
        if count != 2:
            count += 1
            print('Location C is dirty')
            
            # suck and mark clean
            ans = dic[('C',1)]
            if ans == 'Clean':
                Environment.locationCondition['C'] = 0
                score += 1
                print('Location C has been cleaned')
                
                ans1 = dic[('C',0)][0]
                ans2 = dic[('C',0)][1]
                
                # move to D
                if ans1 == 'rotate_right' and ans2 == 'Left':
                    score -= 1
                    print('Rotating')
                    print('Moving to D...')
                
        elif count == 2:
            ans1 = dic[('C',0)][0]
            ans2 = dic[('C',0)][1]

            # move to D
            if ans1 == 'rotate_right' and ans2 == 'Left':
                score -= 1
                print('Rotating')
                print('Moving to D...')
            
    elif Environment.locationCondition['C'] == 0:
        print('Location C is already clean')
        
        ans1 = dic[('C',0)][0]
        ans2 = dic[('C',0)][1]

        # move to D
        if ans1 == 'rotate_right' and ans2 == 'Left':
            score -= 1
            print('Rotating')
            print('Moving to D...')
            
    return score, count
    
##########################################################
    
def roomD(Environment, dic, score, count, home):
    
    # if D is dirty
    if Environment.locationCondition['D'] == 1:
        if count != 2:
            count += 1
            print('Location D is dirty')
            
            # suck and mark clean
            ans = dic[('D',1)]
            if ans == 'Clean':
                Environment.locationCondition['D'] = 0
                score += 1
                print('Location D has been cleaned')
                
                ans1 = dic[('D',0)][0]
                ans2 = dic[('D',0)][1]
                
                # move back to A
                if ans1 == 'rotate_right' and ans2 == 'Up':
                    score -= 1
                    print('Rotating')
                    print('Moving to A...')
                
        elif count == 2:
            ans1 = dic[('D',0)][0]
            ans2 = dic[('D',0)][1]

            # move back to A
            if ans1 == 'rotate_right' and ans2 == 'Left':
                score -= 1
                print('Rotating')
                print('Moving up to A...')
            
    elif Environment.locationCondition['D'] == 0:
        print('Location D is already clean')
        
        ans1 = dic[('D',0)][0]
        ans2 = dic[('D',0)][1]

        # move back to A
        if ans1 == 'rotate_right' and ans2 == 'Up':
            score -= 1
            print('Rotating')
            print('Moving to A...')
            
    if home == True:
    	print('Agent has reached home.')
            
    return score, count
    
##########################################################    
        
class TableDriven(Environment):
    def __init__(self,Environment):
        print(Environment.locationCondition)
        
        #Implement lookup table
        dic = {('A',1):'Clean',('A',0):'Right',('B',1):'Clean',('B',0):['rotate_right','Down'],('C',1):'Clean',('C',0):['rotate_right','Left'],('D',1):'Clean',('D',0):['rotate_right','Up']}
        
        #Instantiate performance measurement
        score = 0
        
        #count variable to maintain 2 dirty place 
        count = 0
            
        # to check if it has returned home
        home = False    
            
#       room A
        home = True
        score, count = roomA(Environment, dic, score, count)
        print('A count',count)
        print('A new condition',Environment.locationCondition['A'])
        print('----------------')

#       room B
        score, count = roomB(Environment, dic, score, count)
        print('B count',count)
        print('B new condition',Environment.locationCondition['B'])
        print('----------------')
        
#       room C
        score, count = roomC(Environment, dic, score, count)
        print('C count',count)
        print('C new condition',Environment.locationCondition['C'])
        print('----------------')
        
#       room D
        score, count = roomD(Environment, dic, score, count, home)
        print('D count',count)
        print('D new condition',Environment.locationCondition['D'])
        print('----------------')
        
        print('Updated LocCondition:',Environment.locationCondition)
        print('Performance measurement: ',str(score))       



if __name__ == '__main__':
        
	td = Environment()
	vac = TableDriven(td)
	




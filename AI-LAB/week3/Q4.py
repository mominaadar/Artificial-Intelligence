import random

###################################################

#         A - B - C
#         D          L-shaped room

class Environment:
    def __init__(self):
        #instantiate locations and conditions

        # 0 is no obstacle, 1 is obstacle
        self.obstacle_ahead = random.randint(0,1)
        self.obstacle_right = random.randint(0,1)
        self.obstacle_left = random.randint(0,1)
        
        self.locationCondition = {'A':'0', 'B':'0', 'C':'0', 'D':'0'}
        
        #randomize conditions in location A, B, C and D
        # 2 indicates Clean and 3 indicated Dirty
        
        self.locationCondition['A'] = random.randint(2,3)
        self.locationCondition['B'] = random.randint(2,3)
        self.locationCondition['C'] = random.randint(2,3)
        self.locationCondition['D'] = random.randint(2,3)
        
###################################################


class TDLshaped(Environment):
    
    def __init__(self,Environment):
        
        print(Environment.locationCondition)
        
        # Implement lookup table
        dic = {('A',3):'Clean',('A',2):{'B':'Right','D':'Down'},('B',3):'Clean',('B',2):{'A':'Left','C':'Right'},('C',3):'Clean',('C',2):'Left',('D',3):'Clean',('D',2):['rotate_right','Up']}
        
        # Instantiate performance measurement
        score = 0
        
        # Whether room has been visited before
        roomA, roomB, roomC, roomD = False, False, False, False
        
        # always starting from A
        score, roomA, roomB, roomC, roomD = rA(Environment, dic, score, roomA, roomB, roomC, roomD)
        print('score after A:',score)
                                               
#         # room B
        score, roomA, roomB, roomC, roomD = rB(Environment, dic, score, roomA, roomB, roomC, roomD)
        print('score after B:',score)
        
        # room C
        rC(Environment, dic, score, roomA, roomB, roomC, roomD)
        
        # room D will be called from room A

        print('Updated LocCondition:',Environment.locationCondition)

###################################################

# ROOM A

def rA(Environment, dic, score, roomA, roomB, roomC, roomD):
        
    obstacle_ahead = random.randint(0,1)
    obstacle_right = random.randint(0,1)
    obstacle_left = random.randint(0,1)
    
    
    if roomA == True:
        print('Agent is coming from room B to A')
        
        print('Moving to D...')
        
        score -= 1
        
        score, roomA, roomB, roomC, roomD = rD(Environment, dic, score, roomA, roomB, roomC, roomD)
        print('Performance measurement: ',str(score))   
        
    else:

        # if A is dirty
        if Environment.locationCondition['A'] == 3:
            print('A is dirty')

            # suck dirt and mark clean
            ans = dic[('A',3)] 
            if ans == 'Clean':
                Environment.locationCondition['A'] = 2
                print('A has been cleaned')
                score += 1
                roomA = True

                #move and check ahead
                if obstacle_ahead == 1:
                    print('Obstacle ahead')

                    #check right
                    print("Checking right")
                    if obstacle_right == 0:
                        print('No obstacle on right')
                        print('Agent moving right')

                        # move to B
                        ans = dic[('A',2)]['B']
                        if ans == 'Right':
                            score -= 1
                            print('Moving to B...')
                            

                    elif obstacle_right == 1:
                        print('Obstacle found on right')

                        #check left
                        print('Checking left')
                        if obstacle_left == 0:
                            print('Agent moving left')

                            # move to B
                            ans = dic[('A',2)]['B']
                            if ans == 'Right':
                                score -= 1
                                print('Moving to B...')
                        else:
                            print('Obstacle found on left')
                            print('Agent moving backward')

                            # move to B
                            ans = dic[('A',2)]['B']
                            if ans == 'Right':
                                score -= 1
                                print('Moving to B...')

                elif obstacle_ahead == 0:
                    print('No obstacle ahead')

                    # move to B
                    ans = dic[('A',2)]['B']
                    if ans == 'Right':
                        score -= 1
                        print('Moving to B...')

        elif Environment.locationCondition['A'] == 2:
            print('A is already clean')
            roomA = True

            #move
            if obstacle_ahead == 1:
                print('Obstacle ahead')

                #check right
                print("Checking right")
                if obstacle_right == 0:
                    print('No obstacle on right')
                    print('Agent moving right')

                    # move to B
                    ans = dic[('A',2)]['B']
                    if ans == 'Right':
                        score -= 1
                        print('Moving to B...')

                elif obstacle_right == 1:
                    print('Obstacle found on right')
                    #check left
                    print('Checking left')

                    if obstacle_left == 0:
                        print('Agent moving left')

                        # move to B
                        ans = dic[('A',2)]['B']
                        if ans == 'Right':
                            score -= 1
                            print('Moving to B...')
                    else:
                        print('Obstacle found on left')
                        print('Agent moving backward')

                        # move to B
                        ans = dic[('A',2)]['B']
                        if ans == 'Right':
                            score -= 1
                            print('Moving to B...')
            elif obstacle_ahead == 0:
                print('No obstacle ahead')

                # move to B
                ans = dic[('A',2)]['B']
                if ans == 'Right':
                    score -= 1
                    print('Moving to B...')
                        
    return score, roomA, roomB, roomC, roomD
    
################################################################

# ROOM B

def rB(Environment, dic, score, roomA, roomB, roomC, roomD):
            
    obstacle_ahead = random.randint(0,1)
    obstacle_right = random.randint(0,1)
    obstacle_left = random.randint(0,1)
    
    
    if roomB == True:
        print('Agent is coming from C to B')
        score -= 1
        rA(Environment, dic, score, roomA, roomB, roomC, roomD)
        
    else:
    
        # if B is dirty
        if Environment.locationCondition['B'] == 3:
            print('B is dirty')

            # suck dirt and mark clean
            ans = dic[('B',3)] 
            if ans == 'Clean':
                Environment.locationCondition['B'] = 2
                print('B has been cleaned')
                score += 1
                roomB = True

                #move and check ahead
                if obstacle_ahead == 1:
                    print('Obstacle ahead')

                    #check right
                    print("Checking right")
                    if obstacle_right == 0:
                        print('No obstacle on right')
                        print('Agent moving right')

                        # move to C
                        ans = dic[('B',2)]['C']
                        if ans == 'Right':
                            score -= 1
                            print('Moving to C...')

                    elif obstacle_right == 1:
                        print('Obstacle found on right')

                        #check left
                        print('Checking left')
                        if obstacle_left == 0:
                            print('Agent moving left')

                            # move to C
                            ans = dic[('B',2)]['C']
                            if ans == 'Right':
                                score -= 1
                                print('Moving to C...')
                        else:
                            print('Obstacle found on left')
                            print('Agent moving backward')

                            # move to C
                            ans = dic[('B',2)]['C']
                            if ans == 'Right':
                                score -= 1
                                print('Moving to C...')

                elif obstacle_ahead == 0:
                    print('No obstacle ahead')

                    # move to C
                    ans = dic[('B',2)]['C']
                    if ans == 'Right':
                        score -= 1
                        print('Moving to C...')

        elif Environment.locationCondition['B'] == 2:
            print('B is already clean')
            roomB = True

            #move and check ahead
            if obstacle_ahead == 1:
                print('Obstacle ahead')

                #check right
                print("Checking right")
                if obstacle_right == 0:
                    print('No obstacle on right')
                    print('Agent moving right')

                    # move to C
                    ans = dic[('B',2)]['C']
                    if ans == 'Right':
                        score -= 1
                        print('Moving to C...')

                elif obstacle_right == 1:
                    print('Obstacle found on right')

                    #check left
                    print('Checking left')

                    if obstacle_left == 0:
                        print('Agent moving left')

                        # move to C
                        ans = dic[('B',2)]['C']
                        if ans == 'Right':
                            score -= 1
                            print('Moving to C...')
                    else:
                        print('Obstacle found on left')
                        print('Agent moving backward')

                        # move to C
                        ans = dic[('B',2)]['C']
                        if ans == 'Right':
                            score -= 1
                            print('Moving to C...')


            elif obstacle_ahead == 0:
                print('No obstacle ahead')

                # move to C
                ans = dic[('B',2)]['C']
                if ans == 'Right':
                    score -= 1
                    print('Moving to C...')
                        
    return score, roomA, roomB, roomC, roomD

################################################################

# ROOM C

def rC(Environment, dic, score, roomA, roomB, roomC, roomD):
        
    obstacle_ahead = random.randint(0,1)
    obstacle_right = random.randint(0,1)
    obstacle_left = random.randint(0,1)
    
    # if C is dirty
    if Environment.locationCondition['C'] == 3:
        print('C is dirty')
        
        # suck dirt and mark clean
        ans = dic[('C',3)] 
        if ans == 'Clean':
            Environment.locationCondition['C'] = 2
            print('C has been cleaned')
            score += 1
            roomC = True
            
            #move and check ahead
            if obstacle_ahead == 1:
                print('Obstacle ahead')
            
                #check right
                print("Checking right")
                if obstacle_right == 0:
                    print('No obstacle on right')
                    print('Agent moving right and rotating')
                    
                elif obstacle_right == 1:
                    print('Obstacle found on right')
                    
                    #check left
                    print('Checking left')
                    if obstacle_left == 0:
                        print('Agent moving left and rotating')
                        
                    else:
                        print('Obstacle found on left')
                        print('Agent moving backward and rotating')
                            
            elif obstacle_ahead == 0:
                print('No obstacle ahead')
            
    elif Environment.locationCondition['C'] == 2:
        print('C is already clean')
        roomC = True

        #move and check ahead
        if obstacle_ahead == 1:
            print('Obstacle ahead')

            #check right
            print("Checking right")
            if obstacle_right == 0:
                print('No obstacle on right')
                print('Agent moving right and rotating')

            elif obstacle_right == 1:
                print('Obstacle found on right')
                
                #check left
                print('Checking left')
                
                if obstacle_left == 0:
                    print('Agent moving left and rotating')
                    
                else:
                    print('Obstacle found on left')
                    print('Agent moving backward and rotating')
                        
                        
        elif obstacle_ahead == 0:
            print('No obstacle ahead')
            print('Agent is rotating')
            
    
    # going back to B
    print('Agent moving back to B')
    score -= 1
    
    rB(Environment, dic, score, roomA, roomB, roomC, roomD)            
    
                        
    return score, roomA, roomB, roomC, roomD        

################################################################

# ROOM D

def rD(Environment, dic, score, roomA, roomB, roomC, roomD):
            
    obstacle_ahead = random.randint(0,1)
    obstacle_right = random.randint(0,1)
    obstacle_left = random.randint(0,1)
    
    # if D is dirty
    if Environment.locationCondition['D'] == 3:
        print('D is dirty')
        
        # suck dirt and mark clean
        ans = dic[('D',3)] 
        if ans == 'Clean':
            Environment.locationCondition['D'] = 2
            print('D has been cleaned')
            score += 1
            roomD = True
            
            #move and check ahead
            if obstacle_ahead == 1:
                print('Obstacle ahead')
            
                #check right
                print("Checking right")
                if obstacle_right == 0:
                    print('No obstacle on right')
                    print('Agent moving right and rotating')
                    
                elif obstacle_right == 1:
                    print('Obstacle found on right')
                    
                    #check left
                    print('Checking left')
                    if obstacle_left == 0:
                        print('Agent moving left and rotating')
                        
                    else:
                        print('Obstacle found on left')
                        print('Agent moving backward and rotating')
                            
            elif obstacle_ahead == 0:
                print('No obstacle ahead')
            
    elif Environment.locationCondition['D'] == 2:
        print('D is already clean')
        roomD = True

        #move and check ahead
        if obstacle_ahead == 1:
            print('Obstacle ahead')

            #check right
            print("Checking right")
            if obstacle_right == 0:
                print('No obstacle on right')
                print('Agent moving right and rotating')

            elif obstacle_right == 1:
                print('Obstacle found on right')
                
                #check left
                print('Checking left')
                
                if obstacle_left == 0:
                    print('Agent moving left and rotating')
                    
                else:
                    print('Obstacle found on left')
                    print('Agent moving backward and rotating')
                        
                        
        elif obstacle_ahead == 0:
            print('No obstacle ahead')
            print('Agent is rotating')
            
    
    # going back to A
    print('Agent moving back to A')
    score -= 1
    
    return score, roomA, roomB, roomC, roomD         

################################################################

        
if __name__ == '__main__':        
        
	td = Environment()
	vac = TDLshaped(td)

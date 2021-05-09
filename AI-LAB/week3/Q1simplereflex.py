import random

class Environment:

    def __init__(self):
   
        #instantiate locations and conditions
        # 0 indicates Clean and 1 indicated Dirty
        self.locationCondition = {'A':'0', 'B':'0'}
        
        #randomize conditions in location A and B
        self.locationCondition['A'] = random.randint(0,1)
        self.locationCondition['B'] = random.randint(0,1)
        
        
        
#we want to take minimum moves to clean rooms so when agent has to move
#to other room it's not good so we decrement score
#and increment score when we clean it to increase performance measurement

class SimpleVacAgent(Environment):

    def __init__(self, Environment):
        print(Environment.locationCondition)
        
        #Instantiate performance measurement
        score = 0
        
        #you can use alphabet A or B for vacuum position randomization
        vacuumLocation = random.randint(ord('A'),ord('B'))
        print('Location:',chr(vacuumLocation))
        
        #vacuum in room A
        if vacuumLocation == ord('A'):
            print('Vacuum is randomly placed in room A')
            
            #if room A is dirty
            if Environment.locationCondition['A'] == 1:
                print("Location A is Dirty")
                
                #suck dirt and mark it clean
                Environment.locationCondition['A'] = 0
                score += 1
                print('Location A has been cleaned')
                
                #move to B
                print('Moving to B...')
                score -= 1
                
                #if B is dirty
                if Environment.locationCondition['B'] == 1:
                    print('Location B is dirty')
                    
                    #suck and mark clean
                    Environment.locationCondition['B'] = 0
                    score += 1
                    print('Location B has been cleaned')
                    
            else:
                #A is clean
                #move to B
                score -= 1
                print('Moving to B...')
                
                #if B is dirty
                if Environment.locationCondition['B'] == 1:
                    print('Location B is dirty')
                    
                    #suck and mark clean
                    Environment.locationCondition['B'] = 0
                    score += 1
                    print('Location B has been cleaned')
                    
        elif vacuumLocation == ord('B'):
            print('Vacuum is placed in room B')
            
            #if room B is dirty
            if Environment.locationCondition['B'] == 1:
                print("Location B is Dirty")
                
                #suck dirt and mark it clean
                Environment.locationCondition['B'] = 0
                score += 1
                print('Location B has been cleaned')
                
                #move to A
                print('Moving to A...')
                score -= 1
                
                #if A is dirty
                if Environment.locationCondition['A'] == 1:
                    print('Location A is dirty')
                    
                    #suck and mark clean
                    Environment.locationCondition['A'] = 0
                    score += 1
                    print('Location A has been cleaned')
                    
            else:
                #B is clean
                #move to A
                score -= 1
                print('Moving to A...')
                
                #if A is dirty
                if Environment.locationCondition['A'] == 1:
                    print('Location A is dirty')
                    
                    #suck and mark clean
                    Environment.locationCondition['A'] = 0
                    score += 1
                    print('Location A has been cleaned')
                    
        #done cleaning
        print(Environment.locationCondition)
        print('Performance measurement: ',str(score))
            
            
if __name__ == '__main__': 

	env = Environment()
	vac = SimpleVacAgent(env)
	
	

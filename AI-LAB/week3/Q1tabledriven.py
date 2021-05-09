import random

class Environment:

    def __init__(self):
    
        #instantiate locations and conditions
        # 0 indicates Clean and 1 indicated Dirty
        self.locationCondition = {'A':'0', 'B':'0'}
        
        #randomize conditions in location A and B
        self.locationCondition['A'] = random.randint(0,1)
        self.locationCondition['B'] = random.randint(0,1)
        
        
        
class TableDrivenVacAgent(Environment):

    def __init__(self,Environment):
    
        print(Environment.locationCondition)
        
        #Implement lookup table
        dic = {('A',1):'Clean', ('A',0):'Right', ('B',1):'Clean',('B',0):'Left'}
        
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
                ans = dic[('A',1)]
                if ans == 'Clean':
                    Environment.locationCondition['A'] = 0
                    score += 1
                    print('Location A has been cleaned')
                
                    #move to B
                    ans = dic[('A',0)]
                    if ans == 'Right':
                        print('Moving to B...')
                        score -= 1

                        #if B is dirty
                        if Environment.locationCondition['B'] == 1:
                            print('Location B is dirty')

                            #suck and mark clean
                            ans = dic[('B',1)]
                            if ans == 'Clean':
                                Environment.locationCondition['B'] = 0
                                score += 1
                                print('Location B has been cleaned')
                                
                        elif Environment.locationCondition['B'] == 0:
                            print('Room B is already clean')
                        
                    
            else:
                #if A is clean move to B
                print('Room A is already clean.')
                ans = dic[('A',0)]
                if ans == 'Right':
                    score -= 1
                    print('Moving to B...')
                
                #if B is dirty
                if Environment.locationCondition['B'] == 1:
                    print('Location B is dirty')
                    
                    #suck and mark clean
                    ans = dic[('B',1)]
                    if ans == 'Clean':
                        Environment.locationCondition['B'] = 0
                        score += 1
                        print('Location B has been cleaned')
                        
                elif Environment.locationCondition['B'] == 0:
                    print('Room B is already clean')
                        
        elif vacuumLocation == ord('B'):
            print('Vacuum is placed randomly in room B')
            
            #if room B is dirty
            if Environment.locationCondition['B'] == 1:
                print("Location B is Dirty")
                
                #suck dirt and mark it clean
                ans = dic[('B',1)]
                if ans == 'Clean':
                    Environment.locationCondition['B'] = 0
                    score += 1
                    print('Location B has been cleaned')
                
                    #move to A
                    ans = dic[('B',0)]
                    if ans == 'Left':
                        print('Moving to A...')
                        score -= 1
                
                        #if A is dirty
                        if Environment.locationCondition['A'] == 1:
                            print('Location A is dirty')

                            #suck and mark clean
                            ans = dic[('A',1)]
                            if ans == 'Clean':
                                Environment.locationCondition['A'] = 0
                                score += 1
                                print('Location A has been cleaned')
                                
                        elif Environment.locationCondition['A'] == 0:
                            print('Room A is already clean')
                    
            else:
                
                #B is clean so move to A
                print('Room B is already clean')
                ans = dic[('B',0)]
                if ans == 'Left':
                    score -= 1
                    print('Moving to A...')
                
                    #if A is dirty
                    if Environment.locationCondition['A'] == 1:
                        print('Location A is dirty')

                        #suck and mark clean
                        ans = dic[('A',1)]
                        if ans == 'Clean':
                            Environment.locationCondition['A'] = 0
                            score += 1
                            print('Location A has been cleaned')
                            
                    elif Environment.locationCondition['A'] == 0:
                            print('Room A is already clean')
                    
        #done cleaning
        print(Environment.locationCondition)
        print('Performance measurement: ',str(score))
        
        
if __name__ == '__main__':
                    
	td = Environment()
	vac = TableDrivenVacAgent(td)
	
	


# --------- MOMINA ATIF DAR - P18-0030 ----------------

import collections
import copy


class Node:
    def __init__(self, key, location, label):
        #four pointers coz any cell can have maximum of 4 possible actions
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        
        self.location = location #tuple of 2D-matrix indices in the form (i,j)
        self.key = key
        self.label = label  #to save which node it is "l" for left, "r" for right, "u" for up and "d" for down

#=======================================================
#CBT
#=======================================================
class graphTree(Node):
    
    # =============================
    def __init__(self, key, location, label, parent=None):
        super().__init__(key, location, label)
        self.parent = parent
        self.rows, self.cols = 5,5  # you can make it nxn matrix
    # =============================
    def get_root(self): 
        """Find the absolute root of the graphTree to which self belongs. 
        Keep going up until you reach no-parent node.
        """
        root = self 
        while root.parent is not None: 
            root = root.parent 

        return root 
        
    # ================================================
    def insert(self,pKey, pLoc, key, location, label):
        '''
        :param key = Node value, location = (i,j) on the 2Dmatrix:
        :pKey, pLoc = parents key, location to search in the tree and then add child node
        :return:pointer of the new node
        '''
        if self.key == pKey and self.location==pLoc:
            
            node = graphTree(key, location, label)  #creating new Node
            node.parent = self #set the parent of this new child
            
            if label=='r':
                self.right = node
                return node
            if label=='l':
                self.left = node
                return node
            if label=='u':
                self.up = node
                return node
            if label=='d':
                self.down = node
                return node

        #left node
        if self.left is not None:
            ans = self.left.insert(pKey,pLoc,key, location, label)
            if ans is not None:
                return ans               
        #right node
        if self.right is not None:
            ans = self.right.insert(pKey,pLoc,key, location, label)
            if ans is not None:
                return ans
        #up node
        if self.up is not None:
            ans = self.up.insert(pKey,pLoc,key, location, label)
            if ans is not None:
                return ans
        #down node
        if self.down is not None:
            ans = self.down.insert(pKey,pLoc,key, location, label)
            if ans is not None:
                return ans
    #==================================
    def findGoalPath(self, node):
        pathCost = 0
        path = {}
        while node.parent is not None: 
            path[node.label] = [node.key, node.location]
            node = node.parent
            pathCost += 1

        #storing labels of all paths in a list
        pathLabels = list(path.keys())
        print("======================\nPath = ", end=" ")
        
        #printing labels in reverse order 
        for i in pathLabels[::-1]:
            print(i, "->", path[i][0], end="  ")
            
        print("\nPath Cost: ",pathCost,"\n===================")    
    # ====================================================
    # Find a node in the tree
    # ====================================================
    # Function for printing Unique Paths from Root-to-Leaf
    @staticmethod
    def print_root_to_leaf(root, path=[]):
        if root is None:
            #print('->'.join([str(x) for x in path]))
            return
        path.append(root.key)
        if root.left is None and root.right is None:
            print('->'.join([str(x) for x in path]))
        else:
            CBT.print_root_to_leaf(root.left, copy.copy(path))
            CBT.print_root_to_leaf(root.right, copy.copy(path))
    
    # =====================================
    #Function for Level-wise printing nodes 
    def level_order_traversal(self, queue):
        '''
        input root node as a list
        print 'level order traversal '
        :return: None
        '''
        queue_new = []
        data = []
        print()
        if not queue:
            return
        else:
            for node in queue:
                #print('<-->', node.key, end='')
                data.append([node.key, (node.location)])
                
                if node.left is not None:
                    queue_new.append(node.left)
                if node.right is not None:
                    queue_new.append(node.right)
                if node.up is not None:
                    queue_new.append(node.up)
                if node.down is not None:
                    queue_new.append(node.down)
                    
            print(' <> '.join([str(x) for x in data]))
        #print('\n________________________')
        self.level_order_traversal(queue_new)
    
    #=============================================
    def possibleActions(self, matrix, key, locations):
        #rows, cols = 5,5
        i , j = locations[0], locations[1]
        
        actions = {}
        #downward
        if i+int(key) in range(0,self.rows): 
            #actions.append((i+key, j))
            actions['d'] = (i+key, j)
        #upward
        if i-int(key) in range(0,self.rows): 
            actions['u'] = (i-key, j)
            #actions.append((i-key, j))
        #right side
        if j+int(key) in range(0,self.cols): 
            #actions.append((i, j+key))
            actions['r'] = (i, j+key)
        #left side
        if j-int(key) in range(0,self.cols): 
            #actions.append((i, j-key))
            actions['l'] = (i, j-key)
        #print("Dictionary: ", actions.items())
        return actions
    #=================================
    def goalTest(self,key, goal):
        if key==goal:
            return True
        else:
            return False
   
   #==========================================
    def A_star(self, matrix, root, goal):

        cost = -1
        total_step_movement = 0
        visited, queue = set(), collections.deque([root])
        visited.add(root)

        while queue:
            min_cost = float('inf')

            explore=True  #set it to by-default True
            print("\n\nA* QUEUE = ", end="")

            for q in queue:
                print(q.key, q.location, end=", ")

    ##################### MY CHANGES #######################

            for q in queue:
                f_n = g_n(q) + heuristic(q)
                print('node:',q.key,q.location,'f_n:',f_n)
                if f_n < min_cost:
                    min_cost = f_n
                    node = q

            print('selected node:',node.key,node.location,'min_cost:',min_cost)    
            
            total_step_movement += min_cost
            
            #Dequeue a Node from queue
            queue.remove(node)

    ##################### MY CHANGES #########################
        
            print("\nExpanding Node: "+ str(node.key) + " ", end="")

            #check if current node is a goal
            if self.goalTest(node.key, goal):
                print("\n\n===================\nHurrah! Found Goal!\n===================\n\n")
                #call to a function: findGoalPath
                #calculating total cost and path from goal-node to the initial state
                self.findGoalPath(node)
                break
                return

            #call to function: possibleActions
            ans = self.possibleActions(matrix, node.key, node.location)
            print("Locations of all possible actions = ", ans)
            cost += 1

            #this function returns an iterable list of 2D-Matrix-indices (i,j) where agent can move next!
            for nextActionDirection, nextActionLoc in ans.items():
                i, j = nextActionLoc[0], nextActionLoc[1]

                newNodeVal = matrix[i][j]
                newNodeLoc = tuple((i,j))
                newNodeLabel = nextActionDirection

                #for first iteration, don't check parent of Root Node; No need

                if cost<=0:
                    print(node.key,node.location,newNodeVal,newNodeLoc, newNodeLabel)

                    newNode = root.insert(node.key,  node.location, newNodeVal, newNodeLoc, newNodeLabel)
                    #print("New node = ", newNode.key, newNode.location)
                    #for the first level
                    visited.add(newNode)
                    queue.append(newNode)

                #check not to add parent of a node under its child
                if cost > 0 and node.parent.location is not newNodeLoc:
                    print(node.key,node.location,newNodeVal,newNodeLoc, newNodeLabel)

                    newNode = root.insert(node.key, node.location, newNodeVal, newNodeLoc, newNodeLabel)

                    #check the neighbours of a node if they're already visited or not
                    #node's can have same value but Unique (row,col) location on matrix
                    for eachNode in visited:
                        if eachNode.location == newNodeLoc:
                            explore=False
                    # If not visited, mark it as visited, and enqueue it
                    if explore:
                        visited.add(newNode)
                        queue.append(newNode)  
                        
        print('Total step movement cost:',total_step_movement)
        
        return None

#==========================================================
    def GBFS(self, matrix, root, goal):

        cost = -1
        total_step_movement = 0
        visited, queue = set(), collections.deque([root])
        visited.add(root)

        while queue:
        
            check_nodes = []
            min_cost = float('inf')

            explore=True  #set it to by-default True
            print("\n\nGBFS QUEUE = ", end="")

            for q in queue:
                print(q.key, q.location, end=", ")

            node = queue.popleft()
        
            print("\nExpanding Node: "+ str(node.key) + " ", end="")

            #check if current node is a goal
            if self.goalTest(node.key, goal):
                print("\n\n===================\nHurrah! Found Goal!\n===================\n\n")
                #call to a function: findGoalPath
                #calculating total cost and path from goal-node to the initial state
                self.findGoalPath(node)
                break
                return

            #call to function: possibleActions
            ans = self.possibleActions(matrix, node.key, node.location)
            print("Locations of all possible actions = ", ans)
            cost += 1

            #this function returns an iterable list of 2D-Matrix-indices (i,j) where agent can move next!
            for nextActionDirection, nextActionLoc in ans.items():
                i, j = nextActionLoc[0], nextActionLoc[1]

                newNodeVal = matrix[i][j]
                newNodeLoc = tuple((i,j))
                newNodeLabel = nextActionDirection

                #for first iteration, don't check parent of Root Node; No need

                if cost<=0:
                    print(node.key,node.location,newNodeVal,newNodeLoc, newNodeLabel)

                    newNode = root.insert(node.key,  node.location, newNodeVal, newNodeLoc, newNodeLabel)
                    #print("New node = ", newNode.key, newNode.location)
                    #for the first level
                    visited.add(newNode)

                #check not to add parent of a node under its child
                if cost > 0 and node.parent.location is not newNodeLoc:
                    print(node.key,node.location,newNodeVal,newNodeLoc, newNodeLabel)

                    newNode = root.insert(node.key, node.location, newNodeVal, newNodeLoc, newNodeLabel)

                    #check the neighbours of a node if they're already visited or not
                    #node's can have same value but Unique (row,col) location on matrix
                    for eachNode in visited:
                        if eachNode.location == newNodeLoc:
                            explore=False
                    # If not visited, mark it as visited, and enqueue it
                    if explore:
                        visited.add(newNode)
                        
       ######################## MY CHANGES ########################
                     
                check_nodes.append(newNode)
                
            for n in check_nodes:
                f_n = heuristic(n)
                print('node:',n.key,n.location,'f_n:',f_n)
                
                if f_n < min_cost:
                    min_cost = f_n
                    newNode = n
                    
            print('selected node:',newNode.key,node.location,'min_cost:',min_cost)
            
            total_step_movement += min_cost
            
            queue.append(newNode)
            
       ######################## MY CHANGES ########################
	
        print('Total step movement cost:',total_step_movement)

        return None

#================================
# g(n) function

def g_n(node):
    cost = 0
    while node.parent:
        cost += 1
        node = node.parent
    return cost
    
#========================
# heuristic function

def heuristic(node):
    
    #manhattan distance
    dx = abs(node.location[1] - 1)
    dy = abs(node.location[0] - 3)
    
    return dx+dy


if __name__ == '__main__':

    #5x5 matrix 
    matrix2D= [
        [3,4,1,3,1],
        [3,3,3,2,2],
        [3,1,2,2,3],
        [4,'G',3,3,3],
        [4,1,4,3,2]
    ]

    ## graphTree Practise   
    b = graphTree(3,(0,0),'y')
    b.A_star(matrix2D, b, 'G')

    print('======================================================================================')

    b.GBFS(matrix2D, b, 'G')

#==============================================================================   

   

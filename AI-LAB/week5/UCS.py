
# Momina Atif Dar - P18-0030

from collections import deque

def print_tree(tree, level=0, label='.'): 
    print(' ' * (level*2) + label + ':' , tree.val)
    for child, lbl in zip([tree.left, tree.right], ['L', 'R']):  # do for all children 
        if child is not None:
            print_tree(child, level+1, lbl)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        
class BST(TreeNode):
    def __init__(self, val, parent=None):
        super().__init__(val)
        self.parent = parent
        
        
    def insert(self, val):
        if val < self.val:
            if self.left is None:
                new_node = BST(val, parent = self)
                self.left = new_node
            else:
                self.left.insert(val)

        elif val > self.val:
            if self.right is None:
                new_node = BST(val, parent = self)
                self.right = new_node
            else:
                self.right.insert(val)
            
            
    # TREE

    def ucs_search(root, goal):
    
        dic = {'R':{'M':1, 'V':5}, 'M':{'F':3, 'O':6}, 'V':{'T':9, 'Y':2}, 'F':{'A':3, 'G':4},'O':{'N':4, 'P':5}, 'T':{'S':8, 'U':6}, 'Y':{'X':7, 'Z':9}}
    
        paths_def = [['R','M','F','A'], ['R','M','F','G'], ['R','M','O','N'], ['R','M','O','P'], ['R','V','T','S'], ['R','V','T','U'], ['R','V','Y','X'], ['R','V','Y','Z']]
    
        # for path to goal state
        path = []
    
        # to keep track of visited nodes
        visited_nodes = []
    
        # to calculate path cost
        cost = 0
        
        que = deque()
        que.append(root)
    
        # if root is goal
        if goal == root.val:
            path.append(root.val)
            return path, cost
    
        # if root is not goal
        while que: 
            current = que.popleft()
        
            # to traverse a node only once
            if current not in visited_nodes:
            
                visited_nodes.append(current.val)
        
                if current.val == goal:
                
                    # loop to get to root from goal state - for path
                    while current:
                        path.append(current.val)
                        current = current.parent
        
                else:            
                    if current.left:
                        que.append(current.left)

                    if current.right:
                        que.append(current.right)
    
        path.reverse()
        
        for i in range(0,len(path)-1):
            first = path[i]
            second = path[i+1]
            cost = cost + dic[first][second]
    
        return path, cost
       
########################################################
 
if __name__ == '__main__':
    
    b = BST('R')
    b.insert('M')
    b.insert('F')
    b.insert('O')
    b.insert('A')
    b.insert('G')
    b.insert('N')
    b.insert('P')
    b.insert('V')
    b.insert('T')
    b.insert('Y')
    b.insert('S')
    b.insert('U')
    b.insert('X')
    b.insert('Z')

    print_tree(b)
    
    path, cost = b.ucs_search('V')
    print('Searching for',path[1])
    print(path, cost)
    print('----------')
    
    
    path, cost = b.ucs_search('Z')
    print('Searching for',path[1])
    print(path, cost)
    
 
 
  


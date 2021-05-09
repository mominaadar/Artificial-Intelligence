
# Momina Atif Dar - P18-0030

def print_tree(tree, level=0, label='.'): 
    print(' ' * (level*2) + label + ':' , tree.val)
    for child, lbl in zip([tree.left, tree.right], ['L', 'R']):  # do for all children 
        if child is not None:
            print_tree(child, level+1, lbl)
            
######################################################

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

######################################################
        
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
            


    def DLS(root, goal, limit):
    
        stk = []
        stk.append(root)
        found = False
    
        while stk:
        
            current = stk.pop()
            #print(current.val)
        
            if current:
                            
                if current.val == goal:
                    found = True
                    break

                else:
                    if current.right:
                        depth = get_depth(current.right)
                        
                        if depth <= limit:
                            stk.append(current.right)
                            
                    if current.left:
                        depth = get_depth(current.left)
                        
                        if depth <= limit:
                            stk.append(current.left)
            
        if found == True:
            depth = get_depth(current)
            print('Goal found at depth',depth)
            return True
            
        else:
            return False



    def IDS(root, goal):
    
        max_depth = 0
        
        # to get max depth
        while root:
            # because CBT so all leaf nodes will be at the same depth
            root = root.left
            if root:
                max_depth += 1
    
        for depth in range(0, max_depth+1):
            flg = b.DLS(goal, depth)
            if flg == True:
                return True

        if flg == False:
            return ('Goal not found')

#########################################################

def get_depth(root):
    level = 0
    
    while root:
        root = root.parent
        if root:
            level += 1
        
    return level

####################################

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

    print('Checking DLS for Z at depth 2:')
    g = b.DLS('Z',2)
    print(g)
    print('-------')
    
    print('Checking DLS for Z at depth 3:')
    g = b.DLS('Z',3)
    print(g)
    print('-------')
    
    print('Checking IDS for O:')
    g = b.IDS('O')
    print(g)
    print('-------')
    
    print('Checking IDS for X:')
    g = b.IDS('X')
    print(g)    
    print('-------')
    
    print('Checking IDS for W:')
    g = b.IDS('W')
    print(g)
    

    
    


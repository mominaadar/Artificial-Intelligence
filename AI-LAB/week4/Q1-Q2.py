
# MOMINA ATIF DAR - P18-0030

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
                
                
    def bfs_search(root, search_key):
        count = 0
        found = False
    
        que = deque()
        que.append(root)
    
        while que:
	
            count += 1
	
            current = que.popleft()
	
            if current.val == search_key:
                found = True
                print('Found')
                print('Total nodes visited:',count)

                return
	
            else:
                if current.left:
                    que.append(current.left)
	        
                if current.right:
                    que.append(current.right)
	        
        if found != True:
            print('Keyword not found')
	
        print('Total nodes visited:',count)
    
        return
        
    
    
    def dfs_search(root, search_key):
    
        stk = []
        stk.append(root)
    
        count = 0
        found = False
	
    
        while stk:
	
            count += 1
            
            current = stk.pop(0)
	
            if search_key == current.val:
	    
                found = True
                print('Found')
                print('Total nodes visited:',count)
                return

            else:
            
                if current.right:
                    stk.append(current.right) 

                if current.left:
                    stk.append(current.left)
	          
	        
        if found != True:
            print('Keyword not found')
	
        print('Total nodes visited:',count)

        return
        
    
    
if __name__ == '__main__':

	b = BST(50)
	b.insert(30)
	b.insert(15)
	b.insert(35)
	b.insert(7)
	b.insert(22)
	b.insert(31)
	b.insert(40)
	b.insert(70)
	b.insert(62)
	b.insert(60)
	b.insert(65)
	b.insert(87)
	b.insert(85)
	b.insert(90)
	
	b.bfs_search(90)
	b.dfs_search(90)




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
	    
        que = deque()
        que.append(root)
    
        while que:
	
            current = que.popleft()
	
            if current.val == search_key:
	    
                print('Found')
                return
	
            else:
                if current.left:
                    que.append(current.left)
		
                if current.right:
                    que.append(current.right)
		
        return 'Key not found'
    


    def dfs_search(root, search_key):
	
        if search_key == root.val:
            print('Found')
        else:
	
            if root.left:
                root.left.dfs_search(search_key)
	    
            if root.right:
                root.right.dfs_search(search_key)    
    
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
	
	



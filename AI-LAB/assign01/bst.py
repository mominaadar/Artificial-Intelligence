
# MOMINA ATIF DAR   P18-0030

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

# dummy class to use in Deletion
class Dummy:
    f = False

        
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

                
    def dfs_preorder(self):
    
        print(self.val)
    
        if self.left:
            self.left.dfs_preorder()
    
        if self.right:
            self.right.dfs_preorder()
        
        return

        
    def dfs_inorder(self):
    
        if self.left:
            self.left.dfs_inorder()
        
        print(self.val)
    
        if self.right:
            self.right.dfs_inorder()
        
        return

        
    def dfs_postorder(self):
    
        if self.left:
            self.left.dfs_postorder()
            
        if self.right:
            self.right.dfs_postorder()
        
        print(self.val)

        return


    def bfs(self):
        lst = [self]
    
        while lst:
            current = lst.pop(0)
            print(current.val)
        
            if current.left:
                lst.append(current.left)
        
            if current.right:
                lst.append(current.right)
                
    # helping function for deletion function            
    def get_successor(self):
        self2 = self
    
        if self.right == None and self.left == None:
            return self2
        else:
            if self.left:
                self2 = self.left.get_successor()
                d.f = True
                return self2
        
            elif self.right:
                if d.f == True:
                    return
                else:
                    self2 = self.right.get_successor()
                    return self2


            

    def delete(self, val):
    
        if self.val == val:
    
            # CASE 1 - only root node
        
            if self.parent is None and self.left is None and self.right is None:
                return None

            # CASE 2 - no child
        
            if self.left is None and self.right is None:   # if child node
            
                if self.parent.right:    # if child node is on the right of parent
                    if self.parent.right.val == val:
                        self.parent.right = None
             
                if self.parent.left:    # if child node is on the left of parent
                    if self.parent.left.val == val:
                        self.parent.left = None
        
           # CASE 3 - one child
    
            if self.left is None and self.right != None:   # if the node to be deleted has only one child on its right
                self.parent.right = self.right

            if self.left != None and self.right is None:   # if the node to be deleted has only one child on its left
                self.parent.left = self.left
                 
            # CASE 4 - two children
        
            if self.right and self.left:
            
                successor = self.right.get_successor()   # find successor/left-most leaf from right subtree
                print('successor of',val,':',successor.val)
                self.delete(successor.val)
                self.val = successor.val
 
        else:
        
            if val < self.val:   # smaller value is on left side
                self.left.delete(val)

            if val > self.val:   # greater value is on right side
                self.right.delete(val)
    
        return


def print_tree(tree, level=0, label='.'): 
    print(' ' * (level*2) + label + ':' , tree.val)
    for child, lbl in zip([tree.left, tree.right], ['L', 'R']):  # do for all children 
        if child is not None:
            print_tree(child, level+1, lbl)
            
            
if __name__ == '__main__':
    d = Dummy()
    t = BST(5)
    t.insert(7)
    t.insert(2)
    t.insert(1)
    t.insert(10)
    t.insert(3)
    t.insert(9)
    t.insert(11)
    t.insert(6)
    print_tree(t)
    
    t.delete(5)
    print_tree(t)
    

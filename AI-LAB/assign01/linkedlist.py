
# MOMINA ATIF DAR   P18-0030


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        ret_str = '['

        temp = self.head
        while temp:
            ret_str += str(temp.val) + ','
            temp = temp.next

        ret_str = ret_str.rstrip(', ')
        ret_str = ret_str + ']'
        return ret_str


    def push(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next != None:
            last = last.next

        last.next = new_node
    


    def removed(self):
        temp = self.head

        if temp is None:
            return 0

        if temp.next is None:
            self.head = None
            return

        while temp.next.next is not None:
            temp = temp.next

        temp.next = None
        temp = None
    
if __name__ == '__main__':

    l = LinkedList()
    l.push(4)
    l.push(8)
    l.push(12)
    l.push(23)
    l.push(1)
    print('After push: ',l)
    
    l.removed()
    print('After deletion: ',l)


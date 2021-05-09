
# MOMINA ATIF DAR   P18-0030


class Stack:
    def __init__(self):
        self.list = []
        
    def push(self, val):
        self.list.append(val)
        
    def pop(self):
        return self.list.pop()
    
    def display(self):
        for i in range(0, len(self.list)):
            print(self.list[i])
            

if __name__ == '__main__':
	s = Stack()
	s.push(4)
	s.push(5)
	s.push(8)
	print('Push:')
	s.display()
	print('----------')
	print('Pop:')
	s.pop()
	s.display()

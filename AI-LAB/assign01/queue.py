
# MOMINA ATIF DAR   P18-0030


class Queue:
    def __init__(self, size=5):
    
        self.queue = []
        self.size = size
        self._inc = 0
        self._dec = 0
        self.Empty = True
        self.Full = False
        
        for i in range(0, self.size):
            self.queue.append(0)
        
        
    def _in(self):
        if self._inc == self.size:
            self._inc = 0
        
        self._inc = self._inc + 1
        return
         
            
    def _out(self):
        if self._dec == self.size:
            self._dec = 0
        
        self._dec = self._dec + 1
        return
        
        
    def enqueue(self, val):
        if self.Full:
            print("List is full")
            return
      
        self.queue[self._inc] = val
        self._in()

        if self._inc == self.size:
            self.Full = True
            self.Empty = False
        return
    
    
    def dequeue(self):
        val = self.queue[self._dec]
        self.queue[self._dec] = 0
        self._out()

        if self._inc == self._dec:
            self.Empty = True

        self.Full = False


        self.shifting()

        self._dec = 0

        return val
    
    
    def shifting(self):

        var1 = self._dec

        for i in range(self.size):

            if self._dec != self.size:

                self.queue[self._dec-1] = self.queue[self._dec]
                self._out()

            else:
                self.queue[self._dec-1] = 0

        self._dec = var1

        return


if __name__ == '__main__':
    q = Queue(6)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(2)
    q.enqueue(45)
    q.enqueue(9)
    
    print('after enqueue ',q.queue)
    
    q.dequeue()
    print('after dequeue ',q.queue)
    
    

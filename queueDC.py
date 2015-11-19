from circularDynamic import *

class QueueDC:
    def __init__(self,value):
        self.capacity = value 
        self.store = dynamicCircular(value)
        self.size = 0

    def enqueue(self,value):
        self.store.addToBack(value)
        return value 

    def dequeue(self):
        return self.store.removeFront()
    
    def peek(self):
        return self.dequeue()
    
    def isEmpty(self):
        return self.store.size == 0

    

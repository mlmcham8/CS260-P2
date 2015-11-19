from Dynamic import *

class stackDynamic:
    def __init__(self, value): 
        self.capacity = value
        self.store = dynamicArray(value)
        self.size = 0

    def push(self,value):
        self.store.addToBack(value)
        return value 

    def pop(self):
        if self.isEmpty():
            raise IndexError('Can\'t pop from empty stack.')
        else:
            return self.store.removeBack()

    def peek(self,value):
        value = self.pop()
        self.push(value)
        return value
    
    def isEmpty(self):
        return self.store.size == 0 

    def isFull(self):
        if self.store != 0:
            return False
    
    def size(self):
        if isEmpty() == False:
            return self.store.size 


from singleLinkedList import *

class stackSingly:
    def __init__ (self):
        self.store = singlyLinkedList()
        self.tail = None
        self.head = None
    
    def push(self, value):
        self.store.addToBack(value)

    def pop(self):
        if self.isEmpty():
            raise IndexError('Can\'t pop from empty stack.')
        else:
            return self.store.removeFront()
        
    def peek(self):
        value = self.pop()
        self.push(value)
        return value

    def isEmpty(self):
        if self.store.size == 0:
            return True 

    def isFull(self):
        if self.store != 0:
            return False

    def size(self):
        return self.store.size


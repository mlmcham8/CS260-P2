from doublyLinkedList import *

class QueueCDLL:
    def __init__(self):
        self.store = doublyLinkedList()
        self.size = 0
    
    def enqueue(self, value):
        self.store.addToBack(value)
        return value

    def dequeue(self):
        return self.store.removeFront()
    
    def peek(self):
        return dequeue()

    def isEmpty(self):
        return self.store.size == 0

    #def isFull(self):
        

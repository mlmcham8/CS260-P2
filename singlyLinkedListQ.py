from singleLinkedList import *

class QueueSLL:
    def __init__(self):
        self.store = singlyLinkedList()
        self.size = 0
        return 

    def enqueue(self,value):
        self.store.addToBack(value)
        return value 

    def dequeue(self):
        return self.store.removeFront()
         

    def peek(self):
        return dequeue()

    def isEmpty(self):
        return self.store.size == 0
        
    
    def isFull(self):
        return False


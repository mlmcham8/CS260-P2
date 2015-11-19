from CircularDLL import *

class Queue:
    def __init__(self):
        self.store = circularDoublyLinkedList()
        self.size = 0

    def enqueue(self,value):
        self.store.addToFront(value)

    def dequeue(self):
        self.store.removeFront()
        
    def peek(self):
        return dequeue()

    def isEmpty(self):
        return self.store.size == 0

    #def isFull()

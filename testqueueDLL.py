from queueDll import *

def main():
    a = doublyLinkedList()
    print('Added 5 values to Front')
    a.addToFront(1)
    a.addToFront(2)
    a.addToFront(3)
    a.addToFront(4)
    a.addToFront(5)
    a.display()
    print()
    print()
    a.removeFront()
    a.removeFront()
    a.removeFront()
    a.removeFront()
    a.display()
    print('Added 5 values to back')
    a.addToBack(1)
    a.addToBack(2)
    a.addToBack(3)
    a.addToBack(4)
    a.addToBack(5)
    a.display()
    print('REMOVE')
    a.removeFront()
    a.removeFront()
    a.removeFront()
    a.removeFront()
    a.display()
    print("start of queue")
    a = QueueCDLL()
    a.enqueue(1)
    a.enqueue(2)
    a.enqueue(3)
    a.enqueue(4)
    a.store.display()
    print()
    a.dequeue()
    a.dequeue()
    a.dequeue()
    a.dequeue()
    a.store.display()
    print()
    a.enqueue(1)
    a.enqueue(2)
    a.enqueue(3)
    a.enqueue(4)
    a.store.display()

main()
 

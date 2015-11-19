from singlyLinkedListQ import *

def main():
    a = Queue()
    a.enqueue(1)
    a.enqueue(2)
    a.enqueue(3)
    a.enqueue(4)
    a.enqueue(5)
    a.enqueue(6)
    a.enqueue(7)
    a.store.display()
    print()
    a.dequeue()
    a.dequeue()
    a.dequeue()
    a.dequeue()
    a.dequeue()
    a.store.display()


main()

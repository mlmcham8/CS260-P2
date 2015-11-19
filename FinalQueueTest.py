from queueDll import *
from queueDC import *
from singlyLinkedListQ import *

def main():
    loop = 1
    while loop != 0:
        print("Your opitions for Queue are:")
        print()
        print("1) Dynamic Circular Class")
        print("2) Singly-Linked List Class")
        print("3) Circular Doubly-Linked List Class")
        print("4) END!")
        print()
        choice = int(input("Which Opition?: "))
        if choice == 1:
            m = int(input("Give a capacity: "))
            a = QueueDC(m)
        elif choice == 2:
            a = QueueSLL()
        elif choice == 3:
            a = QueueCDLL()
        else: 
            break 
        command = 0
        while command != "Q":
            command = input("E for enqueue, D for Deqeue and Q to quit: ")
            if command == 'E':
                value = input("Give value to Enqueue: ")
                a.enqueue(value)
                a.store.display()
                print()
            elif command == 'D':
                print(a.dequeue())
                print("----")
                a.store.display()
                print("Is it Empty:", a.isEmpty())
            else:
                break

    
main()        

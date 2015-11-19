from queueDll import *
from queueDC import *
from singlyLinkedListQ import *

def main():
    loop = 1
    choice = 0
    while loop == 1:
        print("Your opitions for Queue are:")
        print()
        print("1) Dynamic Circular Class")
        print("2) Singly-Linked List Class")
        print("3) Circular Doubly-Linked List Class")
        print("4) END!")
        print()
        choice = int(input("Which opition number? "))
        if choice == 1:
            m = int(input("Give a Capacity for the Dynamic Circular Queue: "))
            a = QueueDC(m)
            command = input("E to enqueue, D to dequeue, Q to quit: ")
            if command == 'E':
                for i in range(0,m):
                    value = input("Give value to enqueue: ")
                    a.enqueue(value)
                    print("Dynamic Circular Queue after:")
                    a.store.display()
                    print()
                    command2 = input("E to enqueue, D to dequeue, Q to quit: ")
                    print()
                    if command2  == 'D':
                        print(a.dequeue())
                        print("Is it Empty:", a.isEmpty())
                        command3 = input("E to enqueue, D to dequeue, Q to quit: ")
                        print()
                        if command3 == 'D':
                            print(a.dequeue())
                            print("Is it Empty:", a.isEmpty())
                            command4 = input("E to enqueue, D to dequeue, Q to quit: ")
                            print()
                            if command4 == 'D':
                                print(a.dequeue())
                                print("Is it Empty:", a.isEmpty())
                            elif command4 == 'Q':
                                break
                        elif command3 == 'Q':
                            break
                    elif command2 == 'Q':
                        break
            elif command == 'D':
                print()
                print('ERROR: Cant dequeue a empty List')
                print()
            else:
                break
        if choice == 2:
            a = QueueSLL()
            print()
            command = input("E to enqueue, D to dequeue, Q to quit: ")
            if command == 'E':
                while command != "Q":
                    value = int(input("Give value to Enqueue to SinglyLinkedList:"))
                    a.enqueue(value)
                    print()
                    print("SinglyLinkedList After:")
                    a.store.display()
                    command2 = input("E to enqueue, D to dequeue, Q to quit: ")
                    if command2  == 'D':
                        print(a.dequeue())
                        print("Is it Empty:", a.isEmpty())
                        command3 = input("E to enqueue, D to dequeue, Q to quit: ")
                        if command3 == 'D':
                            print(a.dequeue())
                            print("Is it Empty:", a.isEmpty())
                            command4 = input("E to enqueue, D to dequeue, Q to quit: ")
                            print()
                            if command4 == 'D':
                                print(a.dequeue())
                                print("Is it Empty:", a.isEmpty())
                            elif command4 == 'Q':
                                break
                        elif command3 == 'Q':
                            break
                    elif command2 == 'Q':
                        break
            elif command == 'D':
                print()
                print("ERROR: Cant dequeue a empty List")
                print()
            else:
                break              
        if choice == 3:
            a = QueueCDLL()
            print()
            command = input("E to enqueue, D to dequeue, Q to quit: ")
            if command == 'E':
                while command != "Q":
                    value = int(input("Give value to Enqueue to Doubly Circular LinkedList:"))
                    a.enqueue(value)
                    print()
                    print("Doubly Circular LinkedList After:")
                    a.store.display()
                    print()
                    command2 = input("E to enqueue, D to dequeue, Q to quit: ")
                    if command2  == 'D':
                        print(a.dequeue())
                        print("Is it Empty:", a.isEmpty())
                        command3 = input("E to enqueue, D to dequeue, Q to quit: ")
                        print()
                        if command3 == 'D':
                            print(a.dequeue())
                            print("Is it Empty:", a.isEmpty())
                            command4 = input("E to enqueue, D to dequeue, Q to quit: ")
                            print()
                            if command4 == 'D':
                                print(a.dequeue())
                                print("Is it Empty:", a.isEmpty())
                            elif command4 == 'Q':
                                break
                        elif command3 == 'Q':
                            break
                    elif command2 == 'Q':
                        break
            elif command == 'D':
                print()
                print("ERROR: Cant dequeue a empty List")
                print()
            else:
                break

        elif choice == 4:
            loop = 0
main()


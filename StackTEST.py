from stack import *
from stackDynamic import *

def main():
    loop = 1
    while loop != 0:
        print("Your opitions for Stack are:")
        print()
        print("1) Dynamic Class")
        print("2) Singly-Linked List Class")
        print("3) END!")
        print()
        choice = int(input("Which Opition?: "))
        if choice == 1:
            m = int(input("Give a capacity: "))
            a = stackDynamic(m)
        elif choice == 2:
            a = stackSingly()
        else:
            break
        command = 0
        while command != "Q":
            command = input("Pu for Push, P for Pop and Q to quit: ")
            if command == 'Pu':
                value = input("Give value to Push: ")
                a.push(value)
                a.store.display()
                print()
            elif command == 'P':
                print(a.pop())
                print("Is it Empty:", a.isEmpty())
            else:
                break


main()


from stackDynamic import *

def main():
    m = int(input("Give me a capacity:"))
    #a = dynamicArray(m)
    #print('Added 5 Values to Back')
    #a.addToBack(1)
    #a.addToBack(2)
    #a.addToBack(3)
    #a.addToBack(4)
    #a.addToBack(5)
    #a.display()
    #print('Is Empty?')
    #print(a.isEmpty())
    #print('Removed 4 values from back')
    #a.removeBack()
    #a.removeBack()
    #a.removeBack()
    #a.removeBack()
    #a.display()
    #print('This is my toArray')
    #print(a.toArray())
    print('This is the Dynamic Stack:')
    b = stackDynamic(m)
    b.push(1)
    b.push(2)
    b.push(3)
    b.push(4)
    b.push(5)
    b.store.display()
    b.pop()
    b.pop()
    b.pop()
    b.pop()
    b.store.display()
    print("The size is:", b.size)
    print('Is Full?')
    print(b.isFull())
    print('Is Empty?')
    print(b.isEmpty())

main()

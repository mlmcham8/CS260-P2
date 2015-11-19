from node import *

class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def addToFront(self,value):
        self.head = Node(value,self.head,self.tail)
        self.head.prev = self.tail
        self.size += 1
        return

    def addToBack(self,value):
        new_node = Node(value,self.head,self.tail)
        if self.tail is None:
            self.head = self.tail = new_node
            new_node.prev = None
            new_node.next = None
        else:
            self.head.prev = new_node
            #new_node.prev = self.tail
            self.tail.next = new_node  
            #new_node.next = self.head
            self.tail = new_node
        self.size += 1
        return

    def removeFront(self):
        tempnode = self.head 
        self.head = self.head.next 
        self.size -= 1
        if self.isEmpty():
            self.tail = None  
        return tempnode.getValue()

    def removeBack(self):
        tempnode = self.tail
        self.tail = self.tail.prev 
        self.tail.next = self.head
        self.size -= 1
        if self.isEmpty():
            self.tail = None 
        return tempnode.getValue()
    
    def insertAtIndex(self,node,index):
        tempnode = self.head
        for i in range(index,0,-1):
            tempnode = tempnode.next 
        node.next = tempnode.next
        tempnode.next = node
        self.size + 1

    def removeAtIndex(self, index):
        if index == 0: 
            value = self.head.value
            self.head = self.nead.next
        else:   
            prev_node = self.Find(index -1)
            value = prev_node.value
            prev_node.next = prev_node.next.next 
        return value 

    def ListIndexNode(values,index):
        node = values
        i = 0
        while i < index and node != None:
            node = Node.next(node)
            i += 1
        if (node == None):
            raise IndexError('true list index' + str(index) + 'is out of bounds')
        return node 

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size

    def Find(self,index):
        node = self.head 
        for i in range(1, index,1):
            node = node.next
        return node.getValue()

    def display(self):
        node = self.head
        #while (node != None):
        print(node.getValue())
        for i in range(1, self.size, 1):
            node = node.next
            print(node.getValue())

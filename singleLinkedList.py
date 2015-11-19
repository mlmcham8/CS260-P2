from node import * 

class singlyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0 

    def addToFront(self,value):
        self.head = Node(value,self.head,None)
        self.size += 1

    def addToBack(self,value):
        new_node = Node(value,self.tail,None)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node 
            new_node.next = None 
        self.size += 1
    
    def removeFront(self):
        tempnode = self.head 
        self.head = self.head.next 
        self.size -= 1
        if self.isEmpty():
            self.tail = None 
        return tempnode.getValue() 
        
    def removeBack(self):
        tempnode = self.tail
        node = self.head
        while(node.next != self.tail):
            node = node.next 
        self.tail = node
        node.next = None
        self.size -= 1
        return tempnode.getValue()

    def insertAtIndex(self,node,index):
        tempnode = self.head
        for i in range(index,0, -1):
            tempnode = tempnode.next
        node = tempnode.next
        tempnode = node 
        self.size += 1
 
    def removeFromIndex(self, index):
        if index == 0:
            value = self.head.value
            self.head  = self.head.next
        else:
            prev_node = self.Find(index - 1)
            value = prev_node.next.value
            prev_node.next = prev_node.next.next
        self.size -= 1 
        return value 
     
    def ListIndexNode(items,index):
        node = items
        i = 0
        while i < index and node != None:
            node = Node.next(node)
            i += 1
        if (node == None):
            raise IndexError("true list index " + str(index) + " is out of bounds")
        return node
 
    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size

    def Find(self, index):
        node = self.head 
        for i in range(1,index,1):
            node = node.next 
        return node.getValue() 

    def display(self):
        node = self.head 
        while (node != None):
            print(node.value)
            node = node.next
        print()
        #print(node.getValue())
        #for i in range(1, self.size):
        #    node = node.next 
        #    print(node.getValue())



def main():
    a = singlyLinkedList()
    a.addToBack(1)
    a.addToBack(2)
    a.addToBack(3)
    a.addToBack(4)
    a.display()
    a.removeFront()
    a.removeFront()
    a.removeFront()
    a.removeFront()
    a.display()
    a.addToBack(1)
    a.addToBack(2)
    a.display()
    return

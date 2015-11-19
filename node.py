class Node(object):
    def __init__(self,value,next,prev):
        self.value = value
        self.next = next
        self.prev = prev

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self,newdata):
        self.value = newdata

    def setNext(self, newnext):
        self.next = newnext

    def setPrev(self, newprev):
        self.prev = newprev

    def getPrev(self):
        return self.prev


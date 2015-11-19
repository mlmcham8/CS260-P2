class dynamicCircular:
    def __init__(self,value):
        self.capacity = value
        self.store= [None] * self.capacity
        self.size = 0
        self.startIndex = 0
        self.endIndex = 0
        self.factor = 2

    def Correct(self, index):
        return (index + self.capacity) % self.capacity

    def normalize(self):
        if(self.size == self.capacity):
            self.grow()
        elif(self.size <= (self.capacity / 2) and self.capacity != 1):
            self.shrink()

    def get(self, index):
        self.spot = self.Correct(index + self.startIndex);
        return self.store[self.spot]

    def set(set, index, value):
        self.spot = self.Correct(index + self.startIndex);
        self.store[self.spot] = value
        return self.store[value]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.capacity == self.size

    def grow(self):
        self.startIndex = 0
        self.capacity = (self.capacity * 2)
        newStore = []
        for i in range(0,int(self.capacity)):
            if (i < len(self.store)):
                newStore.append(self.store[i])
            else:
                newStore.append(None)
        self.store = newStore
        return self.store 

    def shrink(self):
        self.startIndex = 0
        self.capacity = (self.capacity / 2)
        newStore = []
        for i in range(0, int(self.capacity)):
            newStore.append(self.store[i])
        self.store = newStore
        return self.store

    def removeBack(self):
        temp = self.store[self.endIndex]
        self.store[self.endIndex] = None
        self.endIndex = self.Correct(self.endIndex - 1)
        self.size -= 1
        return temp

    def addToBack(self, value):
        if self.isEmpty():
            self.store[self.startIndex] = value 
        else:
            if (self.size == self.capacity):
                self.grow()
            self.endIndex = self.Correct(self.endIndex + 1)
            self.store[self.endIndex] = value
        #self.store[self.size] = value
        self.size += 1
        return

    def removeFront(self):
        temp = self.store[self.startIndex] 
        self.store[self.startIndex] = None 
        self.startIndex = self.Correct(self.startIndex + 1)
        self.size -= 1
        if (self.size == 0):
            self.grow()
        return temp

    def addToFront(self,value):
        self.startIndex = self.Correct(self.startIndex - 1)
        self.store[self.startIndex] = value
        self.size += 1

    def display(self):
        narray = [None] * self.size
        n = self.size
        for i in range(0,self.size,1):
            narray[i] = self.store[n]
            n = self.Correct(n+1)
        return narray

    def Find(self, value):
        count = 0
        current = self.head
        while current != None:
            count += 1
            if current.store == value:
                return count
            else:
                pass
                current = current.next
        return - 1

    def display(self):
        print(self.store)


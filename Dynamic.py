class dynamicArray:
    def __init__(self,value):
        self.capacity = value
        self.store = [None] * self.capacity
        self.size = 0

    def Correct(self,index):
        return (index + self.capacity) % self.capacity

    def get(self,index):
        self.spot = self.normailze(index + self.size);
        return self.store[self.spot]

    def set(self,index,value):
        self.spot = self.normalize(index + self.size);
        self.store[self.spot] = value

    def addToBack(self,value):
        if (self.size == self.capacity):
            self.grow()
        self.store[self.size] = value
        self.size += 1

    def removeBack(self):
        temp = self.store[self.size - 1]
        if(self.size != 0):
            self.size -= 1
            self.store[self.size] = None
            self.normalize()
        return temp

    def normalize(self):
        if(self.size == self.capacity):
            self.grow()
        elif(self.size <= (self.capacity / 2) and self.capacity != 1):
            self.shrink()

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        if self.store != 0:
            return False

    def grow(self):
        self.capacity = (self.capacity * 2)
        newStore = []
        for i in range(0,int(self.capacity)):
            if(i < len(self.store)):
                newStore.append(self.store[i])
            else:
                newStore.append(None)
        self.store = newStore
        #self.capacity += 1 
        

    def shrink(self):
        self.capacity = (self.capacity / 2)
        newStore = []
        for i in range(0,int(self.capacity)):
            newStore.append(self.store[i])
        self.store = newStore

    def toArray(self):
        narray = [None] * self.size
        n = 0
        for i in range(0,self.size,1):
            narray[i] = self.store[n]
            n = self.Correct(n + 1)
        return narray

    def display(self):
        print(self.store)



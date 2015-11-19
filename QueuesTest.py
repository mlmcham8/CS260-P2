from queueDll import *
from scanner import *
from queueDC import *
from singlyLinkedListQ import *

class interpreter():
    def __init__(self):
        self.scanner = Scanner("")
        self.commands = {'"enqueue"' : "self.queue.enqueue(value)", '"dequeue"' : "self.queue.dequeue()", '"new"' : "self.queue = queue", '"display"' : "self.queue.store.display()"}
        self.queue = None 

    def runCommands(self, line):
        self.scanner.fromstring(line)
        EOF = False
        while (EOF == False):
            command = self.scanner.readtoken()
            if(self.validCommand(command) == True):
                self.execute(command)
            elif(command == ""):
                EOF = True
            else:   
                return "Error" 
                    
    def execute(self,command):
        if(self.queue != None or command == '"new"'):
            if(command == '"push"'):
                value = self.scanner.readtoken()
                eval(self.commands['"push"'])
            elif(command == '"new"'):
                queue = self.scanner.readtoken()
                if(queue == '"Circular Dynamic Class"'):
                    value = int(input("Give me a capacity:"))
                    self.queue = QueueDC(value)
                elif(queue == '"Singly-Linked List"'):
                    self.queue = QueueSLL()
                elif(queue == 'Circular Doubly-Linked List'):
                    self.queue = QueueCDLL() 
                else:
                    return "Error"
            else:
                eval(self.commands[command])
        else:
            return "Error"

       
    def validCommand(self,command):
        if(command in self.commands):
            return True
        return False

a = interpreter()
a.runCommands('"new" "Singly-Linked List" "enqueue"" 4 "enqueue" 8 "dequeue" "display" "enqueue" 8 "display" ')
#print("Dynamic Stack Test:")
a.runCommands('"new" "Dynamic" "push" 8 "push" 4 "push" 5 "pop" "display"')
print()

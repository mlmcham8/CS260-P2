from stack import *
from scanner import *
from stackDynamic import *
    
class interpreter():
    def __init__(self):
        self.scanner = Scanner("")
        self.commands = {'"push"' : "self.stack.push(value)", '"pop"' : "self.stack.pop()", '"new"' : "self.stack = stack",'"size"' :"self.stack.size()" , '"display"' : "self.stack.store.display()"}
        self.stack = None 

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
                return "cant"

    def execute(self,command):
        if(self.stack != None or command == '"new"'):
            if(command == '"push"'):
                value = self.scanner.readtoken()
                eval(self.commands['"push"'])
            elif(command == '"new"'):
                stack = self.scanner.readtoken()
                if(stack == '"Dynamic"'):
                    value = int(input("Give me a capacity:"))
                    self.stack = stackDynamic(value)
                elif(stack == '"SinglyLinkedList"'):
                    self.stack = stackSingly()
                else:
                    return "cant"
            else:
                eval(self.commands[command])
        else:
            return "Cant"

        
    def validCommand(self,command):
        if(command in self.commands):
            return True
        return False

    
a = interpreter()
print("SinglyLinkedList Stack Test")
a.runCommands('"new" "SinglyLinkedList" "push" 5 "push" 4 "push" 8 "pop" "display" "push" 8 "display" ')
print("Dynamic Stack Test:")
a.runCommands('"new" "Dynamic" "push" 8 "push" 4 "push" 5 "pop" "display"')
print()



      

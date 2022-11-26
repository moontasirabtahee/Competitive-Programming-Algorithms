# Created by Moontasir Abtahee at 11/26/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here

#Python list can use ase Stack

stack = list()
stack.append(7)
stack.append(6)
stack.append(5)
stack.append(4)
stack.append(3)
stack.append(2)
stack.append(1)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

#creating a stack class here
class Stack:
    def __init__(self):
        self.stack = []
    def printWholeStack(self):
        print(self.stack)
    def push(self,value):
        self.stack.append(value)
    def pushArray(self,array):
        for i in array:
            self.stack.append(i)
    def pop(self):
        return self.stack.pop()
    def popAndPrint(self):
        print(self.pop())
    def length(self):
        return len(self.stack)

# class tester:
#     def __init__(self):
#         newStack = Stack()
#         x = [1,2,3,4,5,6]
#         newStack.pushArray(x)
#         newStack.printWholeStack()
#         newStack.push(7)
#         newStack.popAndPrint()
#
# tester =tester()
# #test passed!
# Created by Moontasir Abtahee at 11/26/2022

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # i want to create an queue using list
# here there will be 2 list
# one will contain the input stack
# then in the second stack we will reverse it thus
# it will become a queue
# FIRST IN FIRST OUT!!!

class Queue:
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def queus(self,value):
        self.inStack.append(value)
    def dequeue(self):
        if not self.outStack:
            self.outStack = self.inStack[::-1]
            self.inStack = []

        return self.outStack.pop()
    def length(self):
        return len(self.inStack) + len(self.outStack)


# queue = Queue()
# queue.queus(1)
# queue.queus(2)
# queue.queus(3)
# queue.queus(4)
# queue.queus(5)
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())

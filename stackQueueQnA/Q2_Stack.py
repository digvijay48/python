#   Created by Elshad Karimov on 04/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.
  
#   Create Stack with min method

class Node():
    def __init__(self, value=None, next = None):
        self.value = value
        self.next = next
    
    def __str__(self):
        string = str(self.value)
        if self.next:
            string += ',' + str(self.next)
        return string

class Stack():
    def __init__(self):
        self.top = None
        self.minNode = None
    
    def min(self):
        if not self.minNode:
            return None
        return self.minNode.value
    
    def push(self, item):
        if self.minNode and (self.minNode.value < item):
            self.minNode = Node(value = self.minNode.value, next=self.minNode)
            print("Inside if Minnode",self.minNode.value)
        else:
            self.minNode = Node(value = item, next=self.minNode)
            print("Inside else Minnode",self.minNode.value)
        self.top = Node(value=item, next=self.top)
    
    def pop(self):
        if not self.top:
            return None
        self.minNode = self.minNode.next
        item = self.top.value
        self.top = self.top.next
        return item

customStack = Stack()
customStack.push(10)
print(customStack.min())
customStack.push(15)
print(customStack.min())
customStack.push(7)
print(customStack.min())
customStack.push(6)
print(customStack.min())
customStack.pop()
customStack.push(42)
customStack.pop()
customStack.pop()
customStack.pop()
print(customStack.min())
customStack.pop()
print(customStack.min())


'''Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"'''
from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    

s = Stack()
str = "We will conquere COVID-19"


for ch in str:
    s.push(ch)

print(s.size())
reverseStr = ''
while s.size() != 0:
    reverseStr += s.pop()

print(reverseStr)
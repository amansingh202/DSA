#stacks using lists

s = []
s.append('https://www.bbc.com/news')
s.append('https://www.bbc.com/business')
s.append('https://www.bbc.com/news/articles/cpv3kz9q167o')
s.append('https://www.bbc.com/news/topics/c1038wnxypvt')

print(s[-1])

print(s.pop())

print(s)

print(s.pop())

#stacks using dequeue

from collections import deque

stack = deque()

print(dir(stack))

stack.append('https://www.bbc.com/news')
stack.append('https://www.bbc.com/business')
stack.append('https://www.bbc.com/news/articles/cpv3kz9q167o')
stack.append('https://www.bbc.com/news/topics/c1038wnxypvt')

print(stack)

print(stack.pop())
print(stack)


#Stack class
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
    


st = Stack()
st.push(5)
st.push(67)
st.push(77)

print(st.peek())

print(st.pop())

print(st.peek())

print(st.is_empty())

print(st.size())
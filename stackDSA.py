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
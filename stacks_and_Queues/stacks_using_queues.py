from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x: int) -> None:
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1, self.q2 = self.q2, self.q1
        

    def pop(self) -> int:
        if self.empty():
            raise IndexError("empty queue")
        else:
            return self.q1.popleft()
        

    def top(self) -> int:
        if self.empty():
            raise IndexError("empty queue")
        else:
            return self.q1[0]

        

    def empty(self) -> bool:
        return not self.q1 
        


# Your MyStack object will be instantiated and called as such:


obj = MyStack()

for i in range(3, 12):
    obj.push(i)

print(obj.pop())

print(obj.top())

print(obj.empty())
class ArrayQueue:
    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)
 

    def pop(self):
        if not self.isEmpty():
            self.queue.pop(0)
        else:
            raise IndexError("empty queue")


    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            raise IndexError("Empty queue")
     

    def isEmpty(self):
        return len(self.queue) == 0
    
que = ArrayQueue()

for i in range(1,6):
    que.push(i)

que.pop()

print(que.peek())



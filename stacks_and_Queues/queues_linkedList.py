class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            

    def pop(self):
        if self.isEmpty():
            raise IndexError("Empty queue")
        else:
            popped_val = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None

            return popped_val

    def peek(self):
        if self.isEmpty():
            raise IndexError("Empty Queue")
        else:
            return self.head.data


    def isEmpty(self):
        return self.head is None
    

que = LinkedListQueue()

for i in range(1, 7):
    que.push(i)

print(que.pop())

print(que.isEmpty())

print(que.peek())

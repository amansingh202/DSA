class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
 

    def pop(self):
        if self.isEmpty():
            raise IndexError("Empty stack")

        popped_val = self.head.data
        self.head = self.head.next
        return popped_val

    def top(self):
        if self.isEmpty():
            raise IndexError("Empty stack")
        else:
            return self.head.data
     

    def isEmpty(self):
        return self.head is None


stack_ll = LinkedListStack()
for i in range(7):
    stack_ll.push(i)

print(stack_ll.pop())

print(stack_ll.top())
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        if self.stack:
            return self.stack.pop()
        else:
            return None
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None
        

    def getMin(self) -> int:
        minimum = float('inf')
        while self.stack:
            top = self.pop()

            if top < minimum:
                minimum = top

        return minimum
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

obj.push(5)
obj.push(3)
obj.push(7)
obj.push(11)

print(obj.getMin())
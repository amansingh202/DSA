class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)
 

    def pop(self):
        if not self.isEmpty():
            self.stack.pop()
        else:
            raise IndexError("pop from empty stack")


    def top(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            raise IndexError("top operation from empty stack")

     

    def isEmpty(self):
        return len(self.stack) == 0


st = ArrayStack()
for i in range(6):
    st.push(i)

st.pop()

print(st.top())
print(st.isEmpty())



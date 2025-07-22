class StockSpanner:

    def __init__(self):
        self.stack = []
        self.index = -1
        

    def next(self, price: int) -> int:
        self.index += 1

        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()

        if not self.stack:
            span = self.index + 1
        else:
            span = self.index - self.stack[-1][1]

        self.stack.append((price, self.index))

        return span
        


# Your StockSpanner object will be instantiated and called as such:
spanner = StockSpanner()
# param_1 = obj.next(price)

print(spanner.next(100))
print(spanner.next(80))   # ➝ 1
print(spanner.next(60))   # ➝ 1
print(spanner.next(70))   # ➝ 2
print(spanner.next(60))   # ➝ 1
print(spanner.next(75))   # ➝ 4
print(spanner.next(85))   # ➝ 6

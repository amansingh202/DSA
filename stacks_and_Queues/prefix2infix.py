class Solution:
    def prefixToInfix(self, s: str) -> str:
        # Your code goes here

        stack = []

        for i in range(len(s)-1, -1, -1):
            if s[i].isalnum():
                stack.append(s[i])
            else:
                t1 = stack.pop()
                t2 = stack.pop()

                con = '(' + t1 + s[i] + t2 + ')'

                stack.append(con)

        return stack[-1]
    
obj = Solution()

print(obj.prefixToInfix("*+pq-mn"))
print(obj.prefixToInfix("+ab"))


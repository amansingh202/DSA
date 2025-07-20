class Solution:
    def postfix2infix(self, s:str) -> str:

        i = 0
        stack = []

        while i < len(s):
            if s[i].isalnum():
                stack.append(s[i])

            else:
                t1 = stack.pop()
                t2 = stack.pop()

                op = '(' + t2 + s[i] + t1 + ')'
                stack.append(op)

            i += 1

        return stack[-1]
        

obj = Solution()

print(obj.postfix2infix("ab-de-f*/"))
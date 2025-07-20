class Solution:
    def prefix2postfix(self, s : str) -> str:
        n = len(s)

        stack = []

        for i in range(n-1, -1, -1):

            if s[i].isalnum():
                stack.append(s[i])
            else:
                top1 = stack.pop()
                top2 = stack.pop()

                con = top1 + top2 + s[i]

                stack.append(con)

        return stack[-1]
    

obj = Solution()

print(obj.prefix2postfix("*+ab-cd"))

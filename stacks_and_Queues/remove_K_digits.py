class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digits in num:
            while stack and stack[-1] > digits and k > 0:
                stack.pop()
                k -= 1

            stack.append(digits)

        while k > 0:
            stack.pop()
            k -= 1

        result = ''.join(stack).lstrip('0')

        return result
    
obj = Solution()

num = "1432219"
k = 3

print(obj.removeKdigits(num, k))
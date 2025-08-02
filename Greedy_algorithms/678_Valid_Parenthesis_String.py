## leetcode 678. Valid Parenthesis String

class Solution:

    ## Brute force approach
    def checkValidString_recursion(self, s: str) -> bool:
        n = len(s)

        def is_valid(s, index, count):
            if count < 0:
                return False
            
            if index == n:
                return count == 0
            
            if s[index] == '(':
                return is_valid(s, index + 1, count + 1)

            if s[index] == ')':
                return is_valid(s, index +1, count - 1)

            if s[index] == '*':
                return is_valid(s, index +1, count + 1) or is_valid(s, index +1, count - 1) or is_valid(s, index +1, count)
            
        return is_valid(s, 0, 0)
    
    ## most optimal greedu approach
    def checkValidString_optimal(self, s: str) -> bool:
        n = len(s)

        min, max = 0, 0

        for i in range(n):
            if s[i] == '(':
                min += 1
                max += 1
            elif s[i] == ')':
                min -= 1
                max -= 1

            else:
                min -= 1
                max += 1

            if min < 0:
                min = 0

            if max < 0:
                return False
            
        return min == 0

    
obj = Solution()

s = "(*))"

print(obj.checkValidString_optimal(s))
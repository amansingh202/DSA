class Solution:
    def checkValidString(self, s: str) -> bool:
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
    
obj = Solution()

s = "(*)("

print(obj.checkValidString(s))
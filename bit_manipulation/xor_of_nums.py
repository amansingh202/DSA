# XOR of numbers in a given range


# 0

# 100
# Medium

# Given two integers L and R. Find the XOR of the elements in the range [L , R].


# Examples:
# Input : L = 3 , R = 5

# Output : 2

# Explanation : answer = (3 ^ 4 ^ 5) = 2.

# Input : L = 1, R = 3

# Output : 0

# Explanation : answer = (1 ^ 2 ^ 3) = 0.

class Solution:      
    def findRangeXOR(self, l, r):
        #your code goes here

        result = 0

        for i in range(l, r+1):
            result = result ^ i

        return result
    
obj = Solution()

print(obj.findRangeXOR(3, 5))
## leetcode 55. Jump Game

class Solution:
    def canJump(self, nums: list[int]) -> bool:

        n = len(nums)

        maximum = 0

        for i in range(n):

            if i > maximum:
                return False
            
            max_index = i + nums[i]

            maximum = max(maximum, max_index)

        return maximum >= n-1
    
obj = Solution()

nums = [3,2,1,0,4]

print(obj.canJump(nums))
        
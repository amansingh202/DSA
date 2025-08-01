## leetcode 45. Jump Game II


## Brute force approach
class Solution:
    def jump(self, nums: list[int]) -> int:

        n = len(nums)

        def jump2(index, jumps):
            if index >= n-1:
                return jumps
            
            minimum = float('inf')
            
            for i in range(1, nums[index] + 1):
                minimum = min(minimum, jump2(index + i, jumps + 1))

            return minimum
        
        return jump2(0,0)

obj = Solution()

nums = [2,3,1,1,4]

print(obj.jump(nums))

        
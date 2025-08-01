## leetcode 45. Jump Game II



class Solution:

    ## Brute force approach
    def jump_brute(self, nums: list[int]) -> int:

        n = len(nums)

        def jump2(index, jumps):
            if index >= n-1:
                return jumps
            
            minimum = float('inf')
            
            for i in range(1, nums[index] + 1):
                minimum = min(minimum, jump2(index + i, jumps + 1))

            return minimum
        
        return jump2(0,0)
    
    ## most optimal approach

    def jump_optimal(self, nums: list[int]) -> int:

        l,r,jumps = 0, 0, 0

        n = len(nums)

        while r < (n-1):
            farthest = 0

            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])

            l = r+1
            r = farthest
            jumps += 1

        return jumps
    


obj = Solution()

nums = [2,3,1,1,4]

print(obj.jump_optimal(nums))

        
class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        n = len(nums)

        count = 0

        for i in range(n):
            sum = 0

            for j in range(i, n):
                sum += nums[j]

                if sum == goal:
                    count += 1

        return count
    
    def numSubarraysWithSum_optimal(self, nums: list[int], goal: int) -> int:
        if goal < 0:
            return 0
        
        l = 0
        r = 0
        sum = 0
        count = 0
        n  = len(nums)

        while r < n:
            sum += nums[r]

            while sum > goal:
                sum = sum - nums[l]
                l = l + 1
            count += (r - l + 1)

            r += 1
        return count

    
obj = Solution()

nums = [0,0,0,0,0]
goal = 0

print(obj.numSubarraysWithSum_optimal(nums, goal))

        
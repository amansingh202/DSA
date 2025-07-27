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
    
obj = Solution()

nums = [0,0,0,0,0]
goal = 0

print(obj.numSubarraysWithSum(nums, goal))

        
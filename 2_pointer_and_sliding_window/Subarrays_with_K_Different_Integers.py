## leetcode 992. Subarrays with K Different Integers

class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:

        n  = len(nums)
        count = 0

        for i in range(n):
            seen = {}

            for j in range(i ,n):
                if nums[j] not in seen:
                    seen[nums[j]] = seen.get(nums[j], 0) + 1

                    if len(seen) == k:
                        count += 1
                    elif len(seen) > k:
                        break

        return count


obj = Solution()
nums = [1,2,1,3,4]
k = 3

print(obj.subarraysWithKDistinct(nums, k))
        
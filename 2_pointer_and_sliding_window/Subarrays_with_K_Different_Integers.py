## leetcode 992. Subarrays with K Different Integers


## brute force approach
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
    
### most optimal approach
    def subarraysWithKDistinct_mostOptimal(self, nums: list[int], k: int) -> int:
        def at_most(k):
            n = len(nums)
            l = 0
            r = 0
            seen = {}
            count = 0

            while r < n:
                seen[nums[r]] = seen.get(nums[r], 0) + 1

                while len(seen) > k:
                    seen[nums[l]] -= 1

                    if seen[nums[l]] == 0:
                        del seen[nums[l]]

                    l = l + 1

                count = count + (r - l + 1)

                r += 1

            return count

        return at_most(k) - at_most(k - 1)

        


obj = Solution()
nums = [1,2,1,2,3]
k = 2

print(obj.subarraysWithKDistinct_mostOptimal(nums, k))
        
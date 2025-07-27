## leetcode 248
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        res = [-1]*n

        for i in range(n):
            if nums[i] %2 == 0:
                res[i] = 0
            else:
                res[i] = 1

        def at_most(k):
            l = 0
            r = 0
            sum = 0
            count = 0

            while r < n:
                sum += (res[r]%2)

                while sum > k:
                    sum = sum - (res[l]%2)
                    l += 1
                count = count + (r - l + 1)

                r += 1

            return count

        return at_most(k) - at_most(k - 1)
    
nums = [2,2,2,1,2,2,1,2,2,2]
k = 2

obj = Solution()

print(obj.numberOfSubarrays(nums, k))

        

        
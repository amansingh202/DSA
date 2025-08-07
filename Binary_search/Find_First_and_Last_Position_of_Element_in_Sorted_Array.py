class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            mid = (l + r)//2

            if nums[mid] == target:
                val = mid
            elif nums[mid] > target:
                l = mid + 1
            else:
                r = mid - 1

            if val and nums[val + 1] == target:
                return (val, val + 1)
            
            return (-1, -1)
        
obj = Solution()

nums = [5,7,7,8,8,10]
target = 8

print(obj.searchRange(nums, target))
        
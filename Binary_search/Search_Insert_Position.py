class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            mid = (l + r)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
            
        return l
        

obj = Solution()

nums = [1,3,5,6]
target = 2

print(obj.searchInsert(nums, target))

        
class Solution:
    def search(self, nums: list[int], target: int) -> int:

        n = len(nums)

        l = 0
        r = n - 1

        while l < r:
            mid = (l + r)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1
        

nums = [-1,0,3,5,9,12]
target = 9

obj = Solution()

print(obj.search(nums, target))


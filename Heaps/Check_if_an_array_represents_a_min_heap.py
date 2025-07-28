class Solution:
    def isHeap(self, nums):
        n = len(nums)

        for i in range(n//2):
            left_child = 2*i + 1
            right_child = 2*i + 2

            if left_child < n and nums[i] > nums[left_child]:
                return False
            
            if right_child < n and nums[i] > nums[right_child]:
                return False
            
        return True
    
obj  = Solution()

nums = [10, 20, 30, 21, 23]

nums2 = [10, 20, 30, 25, 15]

print(obj.isHeap(nums2))
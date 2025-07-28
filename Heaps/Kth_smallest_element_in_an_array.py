import heapq
class Solution:
    def kthSmallestElement(self, nums, k):
        n = len(nums)

        max_heap = [-num for num in nums[:k]]
        heapq.heapify(max_heap)

        for i in range(k, n):
            if nums[i] < -max_heap[0]:
                heapq.heappushpop(max_heap, -nums[i])

        return -max_heap[0]
    
obj = Solution()

nums = [1, 2, 3, 4, 5] 
k = 2

print(obj.kthSmallestElement(nums, k))
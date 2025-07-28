## leetcode 215. Kth Largest Element in an Array


import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        n = len(nums)

        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for i in range(k, n):
            if nums[i] > min_heap[0]:
                heapq.heappushpop(min_heap, nums[i])


        return min_heap[0]
    

obj = Solution()


nums = [3,2,1,5,6,4]
k = 2

print(obj.findKthLargest(nums,k))



        
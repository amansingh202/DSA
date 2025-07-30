## leetcode 347. Top K Frequent Elements

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        minHeap = []

        freq_map = Counter(nums)

        for num, freq in freq_map.items():
            heapq.heappush(minHeap, (freq, num))

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        result = [num for freq, num in minHeap]

        return result
    
obj = Solution()

nums = [1,1,1,2,2,3]
k = 2

print(obj.topKFrequent(nums, k))


        
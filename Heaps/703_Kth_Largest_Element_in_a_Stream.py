## Leetcode : 703. Kth Largest Element in a Stream

import heapq
class KthLargest:

    def __init__(self, k: int, nums: list[int]):

        self.minHeap = nums
        self.k = k

        heapq.heapify(self.minHeap)

        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)


        

    def add(self, val: int) -> int:

        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]


nums = [4,5,8,2]
k = 3      
kth_largest = KthLargest(k, nums)
print(kth_largest.add(3))
import heapq

class Solution:
    def maxSumCombinations(self, nums1, nums2, k):
        nums1.sort(reverse = True)
        nums2.sort(reverse = True)

        n = len(nums1)
        m = len(nums2)

        maxHeap = []
        visited = set()

        heapq.heappush(maxHeap, (-(nums1[0] + nums2[0]), 0 , 0))

        visited.add((0,0))

        result = []

        while maxHeap and len(result) < k:
            neg_sum, i, j = heapq.heappop(maxHeap)

            result.append(-neg_sum)

            if i+1 < n and (i+1, j) not in visited:
                heapq.heappush(maxHeap, (-(nums1[i+1] + nums2[j]), i+1, j))
                visited.add((i+1, j))

            if j+1 < m and (i, j+1) not in visited:
                heapq.heappush(maxHeap, (-(nums1[i]+nums2[j+1]), i, j+1))
                visited.add((i, j+1))

        return result
    
nums1 = [7, 3]
nums2 = [1, 6]
k = 2

obj = Solution()

print(obj.maxSumCombinations(nums1, nums2, k))
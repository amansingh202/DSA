### leetcode 1167_Minimum_Cost_to_Connect_Sticks

import heapq

class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        # Your Code Goes Here

        total_cost = 0
        
        heapq.heapify(sticks)

        while len(sticks) > 1:
            stick1 = heapq.heappop(sticks)
            stick2 = heapq.heappop(sticks)

            combined_sum = stick1 + stick2

            total_cost += combined_sum

            heapq.heappush(sticks, combined_sum)

        return total_cost
    
sticks = [2, 4, 3]

obj = Solution()

print(obj.connectSticks(sticks))



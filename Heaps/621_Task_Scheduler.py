### leetcode 621 Task Scheduler
from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = Counter(tasks)

        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1

            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)

                if count:
                    q.append([count, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
    
tasks = ["A","A","A","B","B","B"]
n = 2

obj = Solution()

print(obj.leastInterval(tasks, n))




        
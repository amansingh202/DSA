## leetcode 56. Merge Intervals

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x: x[0])
        
        n = len(intervals)

        i = 0
        result = []

        

        while i < n:
            start, end = intervals[i]

            while i + 1 < n and intervals[i+1][0] <= end:
                end = max(end, intervals[i+1][1])
                i += 1

            result.append([start, end])

            i += 1

        return result
    
obj = Solution()

intervals = [[1,4],[0,4]]

print(obj.merge(intervals))

        
        
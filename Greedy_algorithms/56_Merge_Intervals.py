class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        n = len(intervals)

        i = 0
        result = []

        intervals.sort(key = lambda x: x[0])

        while i < n:
            start, end = intervals[i]

            while i + 1 < n and intervals[i+1][0] <= end:
                end = max(end, intervals[i+1][1])
                i += 1

            result.append([start, end])

            i += 1

        return result
    
obj = Solution()

intervals = [[1,3],[2,6],[8,10],[15,18]]

print(obj.merge(intervals))

        
        
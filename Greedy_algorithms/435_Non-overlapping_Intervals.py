## leetcode 435. Non-overlapping Intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:

        n = len(intervals)

        intervals.sort(key = lambda x : x[1])


        count = 0
        prev_end_time = 0

        for start, end in intervals:
            if start >= prev_end_time:
                count += 1
                prev_end_time = end

        return (n - count)
    
intervals = [[1,2],[1,2],[1,2]]

obj = Solution()

print(obj.eraseOverlapIntervals(intervals))
        
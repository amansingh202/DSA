class Solution:
    def maxMeetings(self, start, end):
        #your code goes here

        meetings = list(zip(start, end))

        meetings.sort(key = lambda x:x[1])

        count = 0
        max_end_time = 0

        for s, e in meetings:

            if s > max_end_time:
                count += 1
                max_end_time = e

        return count
    
Start = [1, 3, 0, 5, 8, 5] 
End = [2, 4, 6, 7, 9, 9]

obj = Solution()

print(obj.maxMeetings(Start, End))

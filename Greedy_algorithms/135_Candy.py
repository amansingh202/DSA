## leetcode 135. Candy

class Solution:
    def candy(self, ratings: list[int]) -> int:

        n = len(ratings)

        left = [-1]*n
        right = [-1] * n

        left[0], right[n-1] = 1, 1


    ## for left side comparision
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
            else:
                left[i] = 1

        ## for right side comparision

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = 1 + right[i+1]
            else:
                right[i] = 1

        ## taking the maximums

        sum = 0

        for i in range(n):
            sum += max(left[i], right[i])

        return sum
    
obj = Solution()

ratings = [1,0,2]

print(obj.candy(ratings))

        
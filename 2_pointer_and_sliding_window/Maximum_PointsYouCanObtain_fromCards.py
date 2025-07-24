class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        lsum = 0
        rsum = 0
        max_sum = 0
        n = len(cardPoints)

        for i in range(k):
            lsum += cardPoints[i]

        max_sum = lsum

        r_index = n - 1

        for i in range(k-1, -1, -1):
            lsum = lsum - cardPoints[i]
            rsum = rsum + cardPoints[r_index]
            r_index  = r_index -  1

            max_sum = max(max_sum, lsum, lsum + rsum)

        return max_sum
    
cardPoints = [1,79,80,1,1,1,200,1]
k = 3
obj = Solution()
print(obj.maxScore(cardPoints, k))

        
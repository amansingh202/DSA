class Solution:

    # brute force approach O(n^2)
    def totalFruits_brute(self, fruits):
        #your code goes here

        n = len(fruits)

        max_len = 0

        for i in range(n):
            baskets = set()

            for j in range(i, n):
                baskets.add(fruits[j])

                if len(baskets) <= 2:
                    max_len = max(max_len, j-i+1)
                else:
                    break
        return max_len
    
    #better approach O(2n)
    
    def totalFruits_better(self, fruits):
        n = len(fruits)

        max_len = 0
        l = 0
        r = 0
        mpp = {}

        while r < n:
            mpp[fruits[r]] = mpp.get(fruits[r], 0) + 1

            while len(mpp) > 2:
                mpp[fruits[l]] -= 1

                if mpp[fruits[l]] == 0:
                    del mpp[fruits[l]]

                l += 1

            if len(mpp) <= 2:
                max_len = max(max_len, r - l + 1)

            r += 1

        return max_len
    
    # most optimal approach
    def totalFruits_optimal(self, fruits):
        n = len(fruits)
        l = 0
        r = 0
        max_len = 0
        mpp = {}

        while r < n:
            mpp[fruits[r]] = mpp.get(fruits[r], 0) + 1

            if len(mpp) > 2:
                mpp[fruits[l]] -= 1

                if mpp[fruits[l]] == 0:
                    del mpp[fruits[l]]

                l += 1
            
            if len(mpp) <= 2:
                max_len = max(max_len, r - l + 1)

            r += 1

        return max_len




    
obj = Solution()

fruits = [1, 2, 3, 2, 2]

print(obj.totalFruits_optimal(fruits))

        
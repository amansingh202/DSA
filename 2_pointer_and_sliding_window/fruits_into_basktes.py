class Solution:
    def totalFruits(self, fruits):
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
    
obj = Solution()

fruits = [1, 2, 3, 2, 2]

print(obj.totalFruits(fruits))
        
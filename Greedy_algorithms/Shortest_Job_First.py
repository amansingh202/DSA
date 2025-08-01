## Shortest Job First

class Solution:
    def solve(self, bt):
        #your code goes here
        n = len(bt)

        bt.sort()

        wait_time = 0
        t = 0

        for i in range(n):
            wait_time += t
            t += bt[i]

        return wait_time//n

obj = Solution()

bt = [4, 1, 3, 7, 2]

print(obj.solve(bt))
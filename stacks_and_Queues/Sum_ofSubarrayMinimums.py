class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        n = len(arr)

        mod = 10**9 + 7

    #previous smaller element code
        pse = [-1]*n
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            if stack:
                pse[i] = stack[-1]
            else:
                pse[i] = -1

            stack.append(i)

    #next smaller element code

        nse = [n]*n
        stack = []

        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                nse[i] = stack[-1]
            else:
                nse[i] = n

            stack.append(i)

    # code for the problem

        total = 0

        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i

            total = (total + (left * right * arr[i])) % mod

        return total
    

obj = Solution()

arr = [11,81,94,43,3]

print(obj.sumSubarrayMins(arr))
        
class Solution:
    def nextSmallerElements(self, arr):
        # Your code goes here
        n = len(arr)
        nse = [-1]*n
        stack = []

        for i in range(n-1, -1, -1):
            while stack and stack[-1] >= arr[i]:
                stack.pop()

            if stack:
                nse[i] = stack[-1]

            stack.append(arr[i])

        return nse
    

obj = Solution()

arr = [4, 8, 5, 2, 25]

print(obj.nextSmallerElements(arr))
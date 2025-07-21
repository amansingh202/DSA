class Solution:
    def nextLargerElement(self, arr):

        n = len(arr)
        nge = [-1]*n
        stack = []

        for i in range(n-1, -1, -1):
            while stack and arr[i] >= stack[-1]:
                stack.pop()

            if stack:
                nge[i] = stack[-1]

            stack.append(arr[i])


        return nge


   

obj = Solution()

arr = [6, 8, 0, 1, 3]

print(obj.nextLargerElement(arr))
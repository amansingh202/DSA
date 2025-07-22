class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        n = len(heights)

#previous smaller element code
        pse  = [-1]*n
        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                stack.pop()

            if stack:
                pse[i] = stack[-1]
            else:
                pse[i] = -1

            stack.append(i)

#next smaller element code

        nse = [n]*n
        stack= []

        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                nse[i] = stack[-1]
            else:
                nse[i] = n

            stack.append(i)

# code for the maximum rectangle now

        maximum = 0

        for i in range(n):
            maximum = max(maximum, heights[i]*(nse[i] - pse[i] - 1))

        return maximum
    
obj = Solution()

heights = [2,4]

print(obj.largestRectangleArea(heights))

        

        
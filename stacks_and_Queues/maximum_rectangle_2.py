class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        n = len(heights)

        stack= []

        maxArea = 0

        for i in range(n):

            while stack and heights[stack[-1]] > heights[i]:
                element = stack[-1]
                stack.pop()

                nse = i

                pse = stack[-1] if stack else -1

                maxArea = max(maxArea, heights[element] * (nse- pse -1))

            stack.append(i)

        while stack:
            nse = n
            element = stack[-1]

            stack.pop()

            pse = stack[-1] if stack else -1

            maxArea = max(maxArea, heights[element]*(nse - pse -1))

        return maxArea
    
obj = Solution()

heights = [2,4]

print(obj.largestRectangleArea(heights))



        

        
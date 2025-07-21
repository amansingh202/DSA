class Solution:
    def trap(self, height: list[int]) -> int:

        n = len(height)

        leftMax = 0
        rightMax = 0
        total = 0
        left = 0
        right = n-1

        while (left < right):
            if height[left] < height[right]:
                if leftMax > height[left]:
                    total += leftMax - height[left]
                else:
                    leftMax = height[left]

                left += 1
            else:
                if rightMax > height[right]:
                    total += rightMax - height[right]
                else:
                    rightMax = height[right]
                
                right -= 1

        return total

    
obj = Solution()

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(obj.trap(height))



        
        
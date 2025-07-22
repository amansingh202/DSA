class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        
        stack = []

        n = len(asteroids)

        for i in range(n):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroids[i]):
                    stack.pop()

                if stack and stack[-1] == abs(asteroids[i]):
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(asteroids[i])

        return stack
    
obj = Solution()

arr = [-2,-1,1,2]

print(obj.asteroidCollision(arr))
class Solution:
    def celebrity(self, M):
        n = len(M)

        top = 0
        down = n - 1

        while (top < down):
            if M[top][down] == 1:
                top += 1
            elif M[down][top] == 1:
                down -= 1
            else:
                top += 1
                down -= 1

        if top > down:
            return -1
        
        for i in range(n):
            if i == top:
                continue

            if M[i][top] == 0 or M[top][i] == 1:
                return -1
            
        return top
        

obj = Solution()

M = [ [0, 1], [1, 0] ]

print(obj.celebrity(M))
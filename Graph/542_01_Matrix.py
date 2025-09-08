## leetcode 542. 01 Matrix

from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r,c))
                else:
                    mat[r][c] = -1

        directions = [(-1,0), (1,0), (0,1), (0,-1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1
                    q.append((nr, nc))

        return mat
    
sol = Solution()

mat = [[0,0,0],[0,1,0],[0,0,0]]

print(sol.updateMatrix(mat))

mat2 = [[0,0,0],[0,1,0],[1,1,1]]

print(sol.updateMatrix(mat2))

        
## leetcode 994. Rotting Oranges

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        
        minutes = -1

        directions = [(-1,0), (1,0), (0, 1), (0,-1)]

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            minutes += 1

        if fresh == 0:
            return minutes
        else:
            return -1
        
obj = Solution()

print(obj.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))

print(obj.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))

print(obj.orangesRotting([[0,2]]))


        
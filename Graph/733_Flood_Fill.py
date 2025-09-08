## leetcode 733. Flood Fill

from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])

        start_color = image[sr][sc]

        if start_color == color:
            return image
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(r, c):
            image[r][c] = color

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == start_color:
                    dfs(nr, nc)

        dfs(sr, sc)

        return image
    

sol = Solution()

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2

print(sol.floodFill(image, sr, sc, color))
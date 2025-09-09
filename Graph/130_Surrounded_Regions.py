from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                board[r][c] != 'O' or (r, c) in visited):
                return
            visited.add((r, c))
            dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)

        # --- FIX: use 'O' (letter O) on borders ---
        for r in range(rows):
            if board[r][0] == 'O': dfs(r, 0)
            if board[r][cols - 1] == 'O': dfs(r, cols - 1)

        for c in range(cols):
            if board[0][c] == 'O': dfs(0, c)
            if board[rows - 1][c] == 'O': dfs(rows - 1, c)

        # --- FIX: flip 'O' (not '0') that aren't visited ---
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c] = 'X'


# ---------- your test ----------
sol = Solution()

board1 = [["X","X","X","X"],
          ["X","O","O","X"],
          ["X","X","O","X"],
          ["X","O","X","X"]]
sol.solve(board1)
print(board1)   # EXPECTED: [['X','X','X','X'],['X','X','X','X'],['X','X','X','X'],['X','O','X','X']]

board2 = [["X"]]
sol.solve(board2)
print(board2)   # EXPECTED: [['X']]

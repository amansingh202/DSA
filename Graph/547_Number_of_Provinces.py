## leetcode 547. Number of Provinces

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:

        n = len(isConnected)

        visited = set()

        def dfs(city):
            for neighbour in range(n):
                if isConnected[city][neighbour] == 1 and neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)


        provinces = 0

        for city in range(n):
            if city not in visited:
                visited.add(city)
                dfs(city)
                provinces += 1

        return provinces
    
sol = Solution()

print(sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])) 
        
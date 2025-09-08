## strivers code Detect a cycle in an undirected graph using DFS

from collections import deque

class Solution:
    def isCycle(self, V, adj):
        visited = [False] * V

        for start in range(V):
            if visited[start]:
                continue

            stack = [(start, -1)]

            visited[start] = True


            while stack:
                node, parent = stack.pop()

                for neighbour in adj[node]:
                    if not visited[neighbour]:
                        visited[neighbour] = True
                        stack.append((neighbour, node))

                    elif neighbour != parent:
                        return True
                    
        return False
    
sol = Solution()

V1 = 6
adj1 = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
print(sol.isCycle(V1, adj1))

# 2) No cycle
V2 = 4
adj2 = [[1, 2], [0], [0, 3], [2]]
print(sol.isCycle(V2, adj2)) # False
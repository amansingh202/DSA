from collections import defaultdict
from collections import deque
class Solution:

    def dfsOfGraph(self, V, adj):
      source = 0
      stack = [source]
      seen = set([source])
      res = []

      while stack:
        node = stack.pop()
        res.append(node)

        for neighbour in adj[node]:
          if neighbour not in seen:
            seen.add(neighbour)
            stack.append(neighbour)
      return res

        
    
    def bfsOfGraph(self, V, adj):
      source = 0
      q = deque()
      q.append(source)
      seen = set([source])
      res = []

      while q:
        node = q.popleft()
        res.append(node)

        for neighbour in adj[node]:
          if neighbour not in seen:
            seen.add(neighbour)
            q.append(neighbour)

      return res
    
sol = Solution()

V = 5
adj = [[2, 3, 1], [0], [0, 4], [0], [2]]

print("DFS:", sol.dfsOfGraph(V, adj))  # [0, 2, 4, 3, 1]
print("BFS:", sol.bfsOfGraph(V, adj))  # [0, 2, 3, 1, 4] test part


      
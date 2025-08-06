## Minimum time taken to burn the BT from a given Node

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def timeToBurnTree(self, root, start):
        #your code goes here
        if not root:
            return 0
        
        parent = {}

        def dfs(node, par=None):
            if node:
                parent[node] = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        ## find the target node

        def target(node):

            if not node:
                return None
            
            if node.data == start:
                return node
            
            return target(node.left) or target(node.right)
        
        target_node = start

        if not target_node:
            return 0

        ## max time calculation

        queue = deque([(target_node, 0)])
        visited = set([target_node])

        max_time = 0

        while queue:
            node, time = queue.popleft()

            max_time = max(max_time, time)

            for neighbour in [node.left, node.right, parent.get(node)]:
                if neighbour and neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, time + 1))

        return max_time
    
root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)

start = root.right.right


obj = Solution()

print(obj.timeToBurnTree(root, start))




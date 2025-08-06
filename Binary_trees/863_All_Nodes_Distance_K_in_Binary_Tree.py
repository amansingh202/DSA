## leetcode 863. All Nodes Distance K in Binary Tree

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        if not root:
            return []
        
        parent = {}

        def dfs(node, par = None):
            if node:
                parent[node] = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        queue = deque([(target, 0)])
        visited = set([target])
        result = []

        while queue:
            node, distance = queue.popleft()

            if distance == k:
                result.append(node.val)
            elif distance < k:
                for neighbour in (node.left, node.right, parent[node]):
                    if neighbour and neighbour not in visited:
                        visited.add(neighbour)
                        queue.append((neighbour, distance+1))

        return result
    
root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)

target = root.right.right
k =2

obj = Solution()

print(obj.distanceK(root, target, k))


            


        
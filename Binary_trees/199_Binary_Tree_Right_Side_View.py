## leetcode 199. Binary Tree Right Side View

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root) -> list[int]:
        if not root:
            return []
        
        queue = deque([(root, 0)])

        right_nodes = {}

        while queue:
            node, vd = queue.popleft()

            right_nodes[vd] = node.val

            if node.left:
                queue.append((node.left, vd + 1))
            
            if node.right:
                queue.append((node.right, vd + 1))

        return [right_nodes[vd] for vd in sorted(right_nodes)]
    
obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

print(obj.rightSideView(root))
        
        
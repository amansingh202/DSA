

## leetcode 104. Maximum Depth of Binary Tree

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0

        queue = deque([root])

        result = []

        while queue:
            level = []
            
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return len(result)
    
    def maxDepth_recursive(self, root) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth_recursive(root.left), self.maxDepth_recursive(root.right))
    
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    
obj = Solution()

print(obj.maxDepth_recursive(root))


        

        
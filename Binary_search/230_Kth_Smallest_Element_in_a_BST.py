## leetcode 230. Kth Smallest Element in a BST

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.count = 0
        self.result = None

        def dfs(node):
            if not node:
                return None
            
            dfs(node.left)

            self.count += 1

            if self.count == k:
                self.result = node.val
                return
            
            dfs(node.right)

        dfs(root)
        return self.result
    
root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)

obj = Solution()

print(obj.kthSmallest(root, 3))
            

        
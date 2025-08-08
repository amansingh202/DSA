## leetcode 98. Validate Binary Search Tree

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, minVal, maxVal):
            if not node:
                return True
            
            if node.val <= minVal or node.val >= maxVal:
                return False
            
            return validate(node.left, minVal, node.val) and validate(node.right, node.val, maxVal)
        
        return validate(root, float('-inf'), float('inf'))
    
root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(16)

obj = Solution()

print(obj.isValidBST(root))
        
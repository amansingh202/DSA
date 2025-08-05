## leetcode 101. Symmetric Tree

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        if not root:
            return True
        
        def is_mirror(left, right):

            if not left and not right:
                return True
            
            if not left or not right:
                return False
            
            return (left.val == right. val and is_mirror(left.left, right.right) and is_mirror(left.right, right.left))
        
        return is_mirror(root.left, root.right)
    
obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.right.right = TreeNode(5)

print(obj.isSymmetric(root))
        
        

            
        

        
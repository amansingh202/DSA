## strivers code Children Sum Property in Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkChildrenSum(self, root) -> bool:
        # Your code goes here

        if not root or (not root.left and not root.right):
            return True
        
        if root.left:
            left_val = root.left.val
        else:
            left_val = 0

        if root.right:
            right_val = root.right.val
        else:
            right_val = 0

        if root.val != left_val + right_val:
            return False
        
        return self.checkChildrenSum(root.left) and self.checkChildrenSum(root.right)
    
root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)

obj = Solution()

print(obj.checkChildrenSum(root))
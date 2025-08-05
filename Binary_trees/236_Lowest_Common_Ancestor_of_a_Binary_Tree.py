## leetcode 236. Lowest Common Ancestor of a Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root or root.val == p or root.val == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)

        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        
        if left:
            return left
        else:
            return right
        
obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)

p = root.left.left
q = root.right.right

print(obj.lowestCommonAncestor(root, 4, 5).val)
        
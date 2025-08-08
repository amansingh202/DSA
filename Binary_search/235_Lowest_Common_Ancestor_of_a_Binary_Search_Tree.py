## leetcode 235. Lowest Common Ancestor of a Binary Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root:
            return None
        
        curr = root

        if curr.val < p.val and curr.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        if curr.val > p.val and curr.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        return root.val
    
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
p = root.left.right.left
q = root.left

print(obj.lowestCommonAncestor(root, p, q))
        
        
        
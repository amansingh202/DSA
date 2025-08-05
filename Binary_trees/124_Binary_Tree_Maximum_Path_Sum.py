## leetcode 124. Binary Tree Maximum Path Sum

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root) -> int:
        self.maximum = float('-inf')

        def is_node(root):
            if not root:
                return 0
            
            lh = max(0, is_node(root.left))
            rh = max(0, is_node(root.right))

            self.maximum = max(self.maximum, root.val + lh + rh)

            return (root.val + max(lh, rh))
        

        is_node(root)
        return self.maximum
    
obj = Solution()
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

print(obj.maxPathSum(root))
        
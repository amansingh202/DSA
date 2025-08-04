## leetcode 110. Balanced Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        def is_check(node):
            if not node:
                return 0
            lh = is_check(node.left)
            rh = is_check(node.right)

            if lh == -1 or rh == -1 or abs(lh - rh) > 1:
                return -1

            return 1 + max(lh, rh)

        return is_check(root) != -1
    
obj = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

print(obj.isBalanced(root))
        
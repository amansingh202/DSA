## leetcode 700. Search in a Binary Search Tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        while (root and root.val != val):
            if val < root.val:
                root = root.left
            else:
                root = root.right

        return root
    
    def print_tree(self, root):
        if not root:
            return "Tree Not found"
        else:
            return "Tree found"
        
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

# Create solution object
sol = Solution()

result = sol.searchBST(root, 5)

print(sol.print_tree(result))
        
        
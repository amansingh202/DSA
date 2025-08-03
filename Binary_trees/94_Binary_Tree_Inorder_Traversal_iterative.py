## ## leetcode 94. Binary Tree Inorder Traversal Iterative approach

### left -----> root ------> right

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder(self, root):

        if not root:
            return []
        
        result = []
        stack = []

        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result
    
root = TreeNode(4)
root.left = TreeNode(2, TreeNode(1), TreeNode(3))
root.right = TreeNode(6, TreeNode(5), TreeNode(7))

obj = Solution()

print(obj.inorder(root))


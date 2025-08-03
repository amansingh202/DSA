## leetcode 144 pre-order traversal using iterative

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorder(self, root):
        #your code goes here
        if not root:
            return []
        
        result = []

        stack = []

        stack.append(root)

        while stack:
            node = stack.pop()

            result.append(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return result
    
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

obj = Solution()

print(obj.preorder(root))


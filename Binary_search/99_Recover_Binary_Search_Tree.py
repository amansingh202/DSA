## leetcode 99. Recover Binary Search Tree
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first, self.last, self.middle, self.prev = 0, 0, 0, 0

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)

            if self.prev and node.val < self.prev.val:
                if not self.first:
                    self.first, self.middle = self.prev, node
                else:
                    self.last = node

            self.prev = node

            inorder(node.right)

        inorder(root)

        if self.first and self.last:
            self.first.val, self.last.val = self.last.val, self.first.val

        else:
            self.first.val, self.middle.val = self.middle.val, self.first.val

    def print_tree(self, root):
        result = []
        def traverse(root):
            if root:
                traverse(root.left)
                result.append(root.val)
                traverse(root.right)
        traverse(root)

        return result
    
root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(6)
root.left.right = TreeNode(1)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)

obj = Solution()

print("before fixing", obj.print_tree(root))

obj.recoverTree(root)
print("after fixing", obj.print_tree(root))        
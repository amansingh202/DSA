## leetcode 701. Insert into a Binary Search Tree

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        current = root

        while (True):
            if val > current.val:
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(val)
                    break
            else:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(val)
                    break

        return root
    
    def inorder_print(self, root):

        if root:
            self.inorder_print(root.left)
            print(root.val, end = '->')
            self.inorder_print(root.right)

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
result = obj.insertIntoBST(root, 9)

obj.inorder_print(result)
            
        
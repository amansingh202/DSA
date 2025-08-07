## leetcode 450. Delete Node in a BST

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:

            ## no children
            if not root.left and not root.right:
                return None
            
            ## if one children
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            

            ## two children
            successor = self.getMinValueNode(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
        
        return root

    def getMinValueNode(self, node):
        current = node
        while current.left:
            current = current.left

        return current
    
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end ='->')
            self.inorder(root.right)

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

result = obj.deleteNode(root, 7)

print(obj.inorder(result))


    


            
        
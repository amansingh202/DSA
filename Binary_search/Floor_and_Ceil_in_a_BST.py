## strivers code Floor and Ceil in a BST

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def floorCeilOfBST(self, root, key):
        #your code goes here
        
        ##code for ceil

        ceil = -1
        floor = -1

        while root:

            if root.data == key:
                ceil = root.data
                floor = root.data
                return floor, ceil
            elif root.data < key:
                floor = root.data
                root = root.right
            else:
                ceil = root.data
                root = root.left

        return floor, ceil

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
print(obj.floorCeilOfBST(root, 9))
        

        
## leetcode premium Inorder successor and predecessor in BST

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def succPredBST(self, root, key):
        #your code goes here
        suc, pre = -1, -1

        current = root

        while current:
            if key < current.data:
                suc = current.data
                current = current.left

            elif key > current.data:
                pre = current.data
                current = current.right

            else:

                if current.left:
                    temp = current.left

                    while temp.left:
                        temp = temp.left

                    pre = temp.data

                if current.right:
                    temp = current.right

                    while temp.right:
                        temp = temp.right

                    suc = temp.data
                
                break

        return [pre, suc]
    
root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)


key = 7

obj = Solution()

print(obj.succPredBST(root, key))
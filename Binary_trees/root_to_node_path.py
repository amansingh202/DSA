

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def allRootToLeaf(self, root, target):
        #your code goes here

        path = []

        def in_order(node):

            if not node:
                return False
            if in_order(node.left):
                return True
            
            path.append(node.data)

            if node.data == target:
                return True
            
            if in_order(node.right):
                return True
            
            path.pop()

            return False
        
        in_order(root)

        return path
    
obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
target = 5

print(obj.allRootToLeaf(root, target))
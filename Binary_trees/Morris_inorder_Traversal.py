## strivers code Morris Inorder Traversal

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def morrisInorderTraversal(self, root):
        #your code goes here
        result = []
        current = root

        while current:
            if not current.left:
                result.append(current.data)
                current = current.right
            else:
                prev = current.left

                while(prev.right and prev.right != current):
                    prev = prev.right
                
                if not prev.right:
                    prev.right = current
                    current = current.left
                else:
                    prev.right = None
                    result.append(current.data)
                    current = current.right

        return result
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Run Morris Inorder Traversal
obj = Solution()
print(obj.morrisInorderTraversal(root))

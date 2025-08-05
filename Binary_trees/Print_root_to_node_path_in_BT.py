## leetcode Print root to node path in BT

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def allRootToLeaf(self, root):
        #your code goes here

        result = []

        def pre_order(node, path):

            if not node:
                return
            
            path.append(node.data)
            
            if not node.left and not node.right:
                result.append(path[:])

            else:
                pre_order(node.left, path)
                pre_order(node.right, path)

            path.pop()

        pre_order(root, [])

        return result
    
obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)

print(obj.allRootToLeaf(root))
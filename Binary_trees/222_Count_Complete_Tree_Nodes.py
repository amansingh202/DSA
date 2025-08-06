## leetcode 222. Count Complete Tree Nodes



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root) -> int:

        traversal = []

        def pre_order(node):
            if node:
                traversal.append(node.val)
                pre_order(node.left)
                pre_order(node.right)

            
        
        pre_order(root)

        return len(traversal)
    
root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
obj = Solution()
print(obj.countNodes(root))







        
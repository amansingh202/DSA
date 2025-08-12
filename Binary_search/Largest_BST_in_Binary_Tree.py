## strivers code Largest BST in Binary Tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


class Solution:
    def largestBST(self, root):
        #your code goes here //

        self.max_size = 0

        def helper(node):
            if not node:
                return float('inf'), float('-inf'), 0, True
        
            l_min, l_max, l_size, l_is_bst = helper(node.left)
            r_min, r_max, r_size, r_is_bst = helper(node.right)

            if l_is_bst and r_is_bst and l_max < node.data < r_min:
                size = l_size + r_size + 1
                self.max_size = max(self.max_size, size)
                return min(l_min, node.data), max(r_max, node.data), size, True
            
            else:
                return 0, 0, max(l_size, r_size), False
            
        helper(root)
        return self.max_size
    
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

print(obj.largestBST(root))


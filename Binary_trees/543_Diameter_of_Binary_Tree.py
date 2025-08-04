

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        maximum = [0]

        def height(node):
            if not node:               # ✅ base case
                return 0

            lh = height(node.left)
            rh = height(node.right)

            maximum[0] = max(maximum[0], lh + rh)

            return 1 + max(lh, rh)
        
        height(root)
        return maximum[0]


# Test tree
obj = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

print(obj.diameterOfBinaryTree(root))  # Output should be 3

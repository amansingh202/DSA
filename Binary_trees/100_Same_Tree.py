## leetcode 100. Same Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:

        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    

# p = [1,2,3]
# q = [1,2,3]

# Build Tree p: [1, 2, 3]
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

# Build Tree q: [1, 2, 3]
q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

# Check if same
obj = Solution()
print(obj.isSameTree(p, q))  # Output: True
        
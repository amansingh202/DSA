## leetcode 662. Maximum Width of Binary Tree

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root) -> int:

        if not root:
            return 0
        
        max_width = 0

        level_indices = []

        queue = deque([(root, 0)])

        while queue:
            node, index = queue.popleft()

            level_indices.append(index)

            if node.left:
                queue.append((node.left, 2*index))

            if node.right:
                queue.append((node.right, 2*index + 1))

            width = level_indices[-1] - level_indices[0] + 1

            max_width = max(max_width, width)

        return max_width
    
obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)

print(obj.widthOfBinaryTree(root))




        
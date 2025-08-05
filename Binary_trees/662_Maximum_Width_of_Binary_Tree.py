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


        queue = deque([(root, 0)])

        while queue:
            size = len(queue)

            _, level_head_index = queue[0]

            for _ in range(size):
                node, index = queue.popleft()
                index = index - level_head_index

                if node.left:
                    queue.append((node.left, 2*index))

                if node.right:
                    queue.append((node.right, 2*index + 1))

            if queue:
                width = queue[-1][1] - queue[0][1] + 1
            else:
                width = 1

            max_width = max(max_width, width)

        return max_width
            
    
obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)

print(obj.widthOfBinaryTree(root))




        
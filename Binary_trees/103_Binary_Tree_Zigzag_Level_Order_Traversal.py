## leetcode 103. Binary Tree Zigzag Level Order Traversal

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root) -> list[list[int]]:

        if not root:
            return []

        result = []

        queue = deque([root])

        flag  = True

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if not flag:
                level.reverse()

            result.append(level)

            flag = not flag

        return result
    
obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, TreeNode(6))

print(obj.zigzagLevelOrder(root))




        
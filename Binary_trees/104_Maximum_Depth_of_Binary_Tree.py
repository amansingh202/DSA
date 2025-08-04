

## leetcode 104. Maximum Depth of Binary Tree

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root) -> list[list[int]]:
        if not root:
            return None

        queue = deque([root])

        result = []

        while queue:
            level = []
            
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return len(result)
    
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    
obj = Solution()

print(obj.levelOrder(root))


        

        
## leetcode 987. Vertical Order Traversal of a Binary Tree

from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root) -> list[list[int]]:
        if not root:
            return []
        
        queue = deque([(root, 0, 0)])

        nodes = []

        while queue:
            node, col, row = queue.popleft()
            nodes.append((col, row, node.val))

            if node.left:
                queue.append((node.left, col-1, row+1))

            if node.right:
                queue.append((node.right, col+1, row + 1))

        nodes.sort()

        result = defaultdict(list)

        for col, row, val in nodes:
            result[col].append(val)

        return [result[x] for x in sorted(result)]
    
obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, TreeNode(6))

print(obj.verticalTraversal(root))
        
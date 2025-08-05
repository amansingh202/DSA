## Bottom view of BT

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def bottomView(self, root):
        #your code goes here

        if not root:
            return []
        
        bottom_nodes = {}

        queue = deque([(root, 0)])

        while queue:
            node, hd = queue.popleft()

            bottom_nodes[hd] = node.data

            if node.left:
                queue.append((node.left, hd-1))

            if node.right:
                queue.append((node.right, hd + 1))

        return [bottom_nodes[hd] for hd in sorted(bottom_nodes)]
    
obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, TreeNode(6))

print(obj.bottomView(root))




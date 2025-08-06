## leetcode 106. Construct Binary Tree from Inorder and Postorder Traversal

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val : index for index, val in enumerate(inorder)}

        self.post_index = len(inorder) - 1

        def helper(left, right):

            if left > right:
                return None
            
            root_val = postorder[self.post_index]
            self.post_index -= 1

            root = TreeNode(root_val)

            in_index = inorder_map[root_val]

            root.right = helper(in_index+1, right)
            root.left = helper(left, in_index-1)

            return root
        
        return helper(0, len(postorder)-1)
    
    def print_tree(self, root):
        if not root:
            return []
        
        queue = deque([root])
        result = []

        while queue:
            node = queue.popleft()

            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        while result and result[-1] is None:
            result.pop()
        return result

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

obj = Solution()

root = obj.buildTree(inorder, postorder)

print(obj.print_tree(root))


    
    
        
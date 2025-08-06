## leetcode 105. Construct Binary Tree from Preorder and Inorder Traversal

from typing import List, Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        self.pre_index = 0

        def helper(left, right):
            if left > right:
                return None
            
            root_val = preorder[self.pre_index]

            self.pre_index += 1

            root = TreeNode(root_val)

            in_index = inorder_map[root_val]

            root.left = helper(left, in_index-1)
            root.right = helper(in_index+1, right)

            return root
        
        return helper(0, len(preorder)-1)
    
    def print_tree(self,root):
        if not root:
            return []
        result = []
        
        queue = deque([root])

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
    
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

obj = Solution()

root = obj.buildTree(preorder, inorder)

print(obj.print_tree(root))

        

        
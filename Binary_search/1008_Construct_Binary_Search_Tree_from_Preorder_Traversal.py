## leetcode 1008. Construct Binary Search Tree from Preorder Traversal

from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        self.index = 0

        def build(bound):
            if self.index == len(preorder) or preorder[self.index] > bound:
                return None
            
            root_val = preorder[self.index]

            self.index += 1
            root = TreeNode(root_val)

            root.left = build(root_val)
            root.right = build(bound)

            return root
        
        return build(float('inf'))
    
    def print_tree(self, root):
        def in_order(root, traversal):
            if root:
                in_order(root.left, traversal)
                traversal.append(root.val)
                in_order(root.right, traversal)
            
        result = []
        in_order(root, result)
        return result

    
preorder = [8,5,1,7,10,12]

obj = Solution()

root = obj.bstFromPreorder(preorder)

print(obj.print_tree(root))


        
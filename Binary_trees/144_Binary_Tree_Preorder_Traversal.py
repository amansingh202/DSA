## leetcode 144. Binary Tree Preorder Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: optional[TreeNode]) -> list[int]:
        def pre_code(start, traversal):

            if start:
                traversal.append(start.val)
                traversal = pre_code(start.left, traversal)
                traversal = pre_code(start.right, traversal)

            return traversal

        return pre_code(root, [])


        
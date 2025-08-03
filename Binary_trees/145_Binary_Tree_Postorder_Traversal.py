## leetcode 145. Binary Tree Postorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        traversal = []

        def postOrder(root, traversal):
            if root:
                traversal = postOrder(root.left, traversal)
                traversal = postOrder(root.right, traversal)
                traversal.append(root.val)

            return traversal

        return postOrder(root, traversal)
        
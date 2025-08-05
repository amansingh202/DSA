## leetcode premium Boundary Traversal

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def boundary(self, root):
        #your code goes here

        if not root:
            return []
        
        result = []

        def is_leaf(node):
            return not node.left and not node.right
        
        def add_left(node):
            while node:
                if not is_leaf(node):
                    result.append(node.val)
                
                if node.left:
                    node = node.left
                else:
                    node = node.right

        def add_leaves(node):
            if is_leaf(node):
                result.append(node.val)
                return
            if node.left:
                add_leaves(node.left)
            if node.right:
                add_leaves(node.right)

        def add_right(node):
            stack = []

            while node:
                if not is_leaf(node):
                    stack.append(node.val)

                if node.right:
                    node = node.right
                else:
                    node = node.left

            while stack:
                result.append(stack.pop())

        if not is_leaf(root):
            result.append(root.val)

        add_left(root.left)
        add_leaves(root)
        add_right(root.right)

        return result
    
obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, TreeNode(6))

print(obj.boundary(root))



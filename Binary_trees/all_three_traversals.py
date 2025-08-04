## all three traversals

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root) -> list[int]:

        if not root:
            return [], [], []
        
        stack = [(root, 1)]

        preorder, inorder, postorder = [], [], []

        while stack:
            node, state = stack[-1]

            if state == 1:
                preorder.append(node.val)
                stack[-1] = (node, 2)

                if node.left:
                    stack.append((node.left, 1))


            elif state == 2:
                inorder.append(node.val)
                stack[-1] = (node, 3)

                if node.right:
                    stack.append((node.right, 1))

            else:
                postorder.append(node.val)

                stack.pop()

        return preorder, inorder, postorder
    
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, TreeNode(6), TreeNode(7))

obj = Solution()

print(obj.postorderTraversal(root))

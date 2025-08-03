## leetcode 145_Binary_Tree_Postorder_Traversal Iterative approach

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root) -> list[int]:

        if not root:
            return []
        
        stack1, stack2, result =[], [], []

        stack1.append(root)

        while stack1:
            node = stack1.pop()

            stack2.append(node)

            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        while stack2:
            node = stack2.pop()
            result.append(node.val)

        return result
    
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, TreeNode(6), TreeNode(7))

obj = Solution()

print(obj.postorderTraversal(root))

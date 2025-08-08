## leetcode 173. Binary Search Tree Iterator

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.inorder(root)
        

    def next(self) -> int:
        tmp = self.stack.pop()
        self.inorder(tmp.right)
        return tmp.val
        

    def hasNext(self) -> bool:
        return len(self.stack) > 0


    def inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left

root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

bSTIterator = BSTIterator(root)
print(bSTIterator.next())   # 3
print(bSTIterator.next())    # 7
print(bSTIterator.hasNext()) # True
print(bSTIterator.next())    # 9
print(bSTIterator.hasNext()) # True
print(bSTIterator.next() )   # 15
print(bSTIterator.hasNext()) # True
print(bSTIterator.next()  )  # 20
print(bSTIterator.hasNext()) # False





        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
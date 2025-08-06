## leetcode hard 297. Serialize and Deserialize Binary Tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []

        def preorder(node):
            if not node:
                result.append('null')
                return 
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(result)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = data.split(',')
        self.index = 0

        def dfs():
            if self.index >= len(values):
                return None
            
            val = values[self.index]
            self.index += 1

            if val == 'null':
                return None
            
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()

            return node
        return dfs()
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
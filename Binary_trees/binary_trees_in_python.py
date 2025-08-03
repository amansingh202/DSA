class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'pre_order':
            return self.preorder_print(tree.root, "")

    ## preorder traversal DFS

    def preorder_print(self, start, traversal):
        """Root -> left child --> right child"""

        if start:
            traversal += str(start.value) + "--"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)

        return traversal



tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree("pre_order"))


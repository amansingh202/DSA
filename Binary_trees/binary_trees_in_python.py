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
        elif traversal_type == "in_order":
            return self.inorder_traversal(tree.root, "")

    ## Tree structure
    # """                             1
    #                         /                \ 
    #                        2                   3
    #                       /  \                / \
    #                     4      5             6    7     """
                             
    ##pre-order tree traversal code
    def preorder_print(self, start, traversal):
        """Root -> left child --> right child"""
        """ 1->2->4->5->3->6->7"""

        if start:
            traversal += str(start.value) + "--"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)

        return traversal
    
    ## in-order tree traversal code
    def inorder_traversal(self, start, traversal):
        """ left --> root --> right"""
        """ 4--2--5--1--6--3--7"""

        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += str(start.value) + "--"
            traversal = self.inorder_traversal(start.right, traversal)

        return traversal



tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree("pre_order"))

print(tree.print_tree("in_order"))


"""Recursive Preorder Traversal
Given a binary tree, write a function to recursively traverse it in the preorder manner. Mark a node as visited by adding its data to the list - pre_ordered_list(defined globally at the top of the editor).

Example:

     1
    / \
   2   3     ==> 1245367
  / \ / \
 4  5 6  7
"""

pre_ordered_list = []


class BinaryTree:
    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def preorder(self):
        if self.data:
            pre_ordered_list.append(self.data)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()
        return pre_ordered_list
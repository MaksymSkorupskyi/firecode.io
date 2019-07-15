"""Recursive Postorder Traversal
Given a binary tree, implement a method to populate the list post_ordered_list
with the data of the nodes traversed in postorder, recursively.

Example:
     1
    / \
   2   3     ==> 4526731
  / \ / \
 4  5 6  7

"""
post_ordered_list = []


class BinaryTree:
    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def postorder(self) -> list:
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()
        post_ordered_list.append(self.data)
        return post_ordered_list

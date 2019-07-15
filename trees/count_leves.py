"""Count the Leaves!
Write a function to find the total number of leaf nodes in a binary tree.
A node is described as a leaf node if it doesn't have any children.
If there are no leaf nodes, return 0.

Example:
       1
      / \
     2   3
    / \ / \
   4  5 6  7
  / \
 8   9
==> no. of leaves = 5

Algorithm:
1. Recursively traverse the tree.
2. At each node, determine if its left and right child nodes are None.
2a. If True, return 1.
2b. Otherwise, find number of leaves in its left and right subtrees (recursively).
3. Return the sum of the number of leaves in the left and the right subtrees.
"""


class TreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    def number_of_leaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left_child and not root.right_child:
            return 1
        return self.number_of_leaves(root.left_child) + self.number_of_leaves(root.right_child)

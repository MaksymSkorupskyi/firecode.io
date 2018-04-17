"""Reverse a Singly Linked List
Given a singly linked list, write a method to perform In-place reversal.
Example:
1->2->3 ==> 3->2->1

The key here is to reverse the next link to the previous node at each step of the traversal
till you reach the end of the list.

Algorithm:
1. Create a node - last and initialize it to None.
2. Start traversing through the list by marking head node as the current node, till you reach to the end of the list.
3. Within the loop, create a temporary variable next to store the current's next node.
4. Point the next link of the current node to the last node, created in step one.
5. Set last = current and current = next.
6. At the end of the loop, set head = last, which results in the head pointing to the reversed list.
"""

class Node:
    def __init__(self):
        self.data = None
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev_node = None
        curr_node = self.head
        while curr_node:
            next_node = curr_node.next # Remember next node
            curr_node.next = prev_node  # REVERSE! None, first time round.
            prev_node = curr_node  # Used in the next iteration.
            curr_node = next_node  # Move to next node.
        self.head = prev_node
"""Insert a Node at the Front of a Linked List
Write a function to insert a node at the front of a Singly Linked-List

Examples:
LinkedList: 1->2 , Head = 1
insert_at_front(1) ==> 1->1->2
insert_at_front(2) ==> 2->1->2
insert_at_front(3) ==> 3->1->2
"""

class Node:
    def __init__(self):
        self.data = None
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Method for inserting a new node at the start of a Linked List
    def insert_at_front(self, data):
        new_node = Node()
        new_node.data = data
        new_node.next = self.head
        self.head = new_node

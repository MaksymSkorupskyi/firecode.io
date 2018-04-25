"""Inserting a Node at the End of a Singly Linked List
Write a function to insert a node at the end of a Singly Linked-List.

Examples:
LinkedList: 1->2 , Head = 1
insertAtEnd(1) ==> 1->2->1
insertAtEnd(2) ==> 1->2->2
insertAtEnd(3) ==> 1->2->3
Test Inputs:
Nodes To Inserted: 1: 1
Nodes To Inserted: 1, 2, 3, 4, 5: 1->2->3->4->5
Nodes To Inserted: 3, 5: 3->5
Nodes To Inserted: -1, -2, -3: -1->-2->-3

Algorithm:
1) create a Node node with the input data,
2) interate over to the end of the singly linked list
3) append this new node to the end of the list
by setting the next pointer of the last node to point to the newly created node.

1. Create a new Node newNode
2. If head is None, set self.head = newNode.
3. Else, iterate to the last node of the list and set its next pointer to newNode.
"""

class Node:
    def __init__(self):
        self.next = None
        self.data = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # method for inserting a new node at the end of a Linked List
    def insertAtEnd(self, data):
        new_node = Node()
        new_node.data = data
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:  # while curr_node.getNext():
                curr_node = curr_node.next  # curr_node = curr_node.getNext()
            curr_node.next = new_node # curr_node.setNext(newNode)


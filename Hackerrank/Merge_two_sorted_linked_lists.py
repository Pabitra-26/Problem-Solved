# Problem name: Merge two sorted linked lists
"""Description: You’re given the pointer to the head nodes of two sorted linked lists.
The data in both lists will be sorted in ascending order.
Change the next pointers to obtain a single, merged linked list which also has data in ascending order.
Either head pointer given may be null meaning that the corresponding list is empty."""
# Strategy: take three pointers, and initialise two(in this case p and q) to head of both the lists and the other, which will help in sorting

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

def mergeLists(head1, head2):
    p = head1                      # initialise pointer p to head node of first linked lists
    q = head2                      # initialise pointer q to head node of second linked lists
    s = None                       # initialise s to None
    if not p:                      # check if either of the linked lists are empty, if any linked list of empty, then just return the other linked list
        return q
    if not q:
        return p
    if p and q:                   # if neither of the linked lists are empty, then check which of head node data is less
        if (p.data <= q.data):    # if data in head node of p is less, then assign it to s, and point p to the next node in the linked list
            s = p
            p = s.next
        else:                    # similarly with q
            s = q
            q = s.next
    new_head = s                  # since s is pointing to either of the heads, that can be the new head of the final sorted list
    while (p and q):              # now we do the same thing as we iterate through both the lists
        if (p.data <= q.data):
            s.next = p
            s = p
            p = s.next
        else:
            s.next = q
            s = q
            q = s.next

    if not p:                   # if either of the linked lists ends(points to None), then just point to the other list
        s.next = q
    if not q:
        s.next = p
    return new_head            # return the new_head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()

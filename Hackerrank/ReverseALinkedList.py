# Problem name: Reverse a Linked List
# Description: You’re given the pointer to the head node of a linked list. Change the next pointers of the nodes so that their order is reversed. The head pointer given may be null meaning that the initial list is empty.
# Strategy: There are two methods - iterative and recursive...In this code iterative method has been used

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

def reverse(head):                                   # head is passed as an argument
    prev=None                                        # we initialize three different pointers-prev, current and next_n
    current=head
    while(current is not None):                      # we then iterate through the linked list, with values of those 3 pointers changing accordingly as we move forward
        next_n=current.next                          # when current finally becomes NULL, i.e reaches the other end of the linked list
        current.next=prev
        prev=current
        current=next_n
    head=prev                                        # finally the head is the last element of the original linked list
    return head                                      #list is reversed

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()

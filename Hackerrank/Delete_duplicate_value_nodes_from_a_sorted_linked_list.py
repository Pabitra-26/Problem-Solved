# Problem name: Delete duplicate value nodes from a sorted linked list
# Description: You're given the pointer to the head node of a sorted linked list, where the data in the nodes is in ascending order. Delete as few nodes as possible so that the list does not contain any value more than once. The given head pointer may be null indicating that the list is empty.
# Strategy: we will store the values(data values) whenever there is a new one in a dictionary and see if it occurs again in the linked list, if it does, then remove that node

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

def removeDuplicates(head):
    curr=head
    prev=None
    dup_value=dict()     # we will store the unique values here
    while(curr):
        if(curr.data in dup_value):   #  if the same element occurs again in the linked list
            prev.next=curr.next       # break the link
            curr=None                  # point it to none , to delete it
        else:
            dup_value[curr.data]=1     # if it's a new element, then store it in the dictionary and store its value as one
            prev=curr
        curr=prev.next
    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = removeDuplicates(llist.head)

        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()

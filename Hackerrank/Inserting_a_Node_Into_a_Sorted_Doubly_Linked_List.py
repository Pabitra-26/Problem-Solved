# Problem name: Inserting a Node Into a Sorted Doubly Linked List
# Description: Given a reference to the head of a doubly-linked list and an integer,data, create a new DoublyLinkedListNode object
# having data value data and insert it into a sorted linked list while maintaining the sort.
# Strategy: first check if the first node is >data given, if yes, then insert at node
# then iterate through the node, till the second last element, and check where it fits
# if data is still greater than the second last node, then chech whether it is < last node data and insert at the end

import math
import os
import random
import re
import sys


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def sortedInsert(head, data):
    cur = head
    node = DoublyLinkedListNode(data)
    if cur.data > data or cur.data == data:
        node.next = cur
        cur.prev = node
        head = node
        return head
    while cur.next:
        if (cur.data < data and cur.next.data > data) or cur.data == data:
            node.next = cur.next
            cur.next.prev = node
            node.prev = cur
            cur.next = node
            return head
        cur = cur.next
    if cur.data < data or cur.data == data:
        node.prev = cur
        cur.next = node
        return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()

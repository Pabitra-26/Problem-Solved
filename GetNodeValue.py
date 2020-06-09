# Problem name: Get Node Value
# Description: You’re given the pointer to the head node of a linked list and a specific position. Counting backwards from the tail node of the linked list, get the value of the node at the given position. A position of 0 corresponds to the tail, 1 corresponds to the node before the tail and so on.
# Strategy: Either you can reverse linked list and count from the beginning or you can get the length of the linked list, subtract one from it and then subtract the position given from it , to get the position from the beginning

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

def length(head):            # to get the length of the linked list
    count = 0
    itr = head
    while (itr):
        count += 1
        itr = itr.next
    return count


def getNode(head, positionFromTail):
    position = (length(head) - 1) - positionFromTail                   # to get the position from the beginning
    itr = head
    c = 0
    while (itr):
        if (c == position):
            return itr.data                                           # iterate through the linked list till you reach the required position, then return the data element of that node
        itr = itr.next
        c += 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        position = int(input())

        result = getNode(llist.head, position)

        fptr.write(str(result) + '\n')

    fptr.close()

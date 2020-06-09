# Problem name: Compare two Linked Lists
# Description: You’re given the pointer to the head nodes of two linked lists. Compare the data in the nodes of the linked lists to check if they are equal.
"""Strategy: The lists are equal only if they have the same number of nodes and corresponding nodes contain the same data.
 Either head pointer given may be null meaning that the corresponding list is empty."""

import os
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

def length(llist):                   # To get the length of the linked lists
    count = 0                        # initialize a count variable with 0
    itr = llist                      # initialise another variable itr to hold the value in head node, so that we do not the lost the data in head node
    while (itr):                     # iterate through the linked list and increment count variable till itr!=None
        count += 1
        itr = itr.next
    return count                     # return the length of the linked list


def compare_lists(llist1, llist2):

    m = length(llist1)                        # get the lengths
    n = length(llist2)
    if (m != n):                              # if lengths of both the linked lists are not same then they are not equal
        return 0
    else:                                     # if the lengths are same
        itr1 = llist1
        itr2 = llist2
        while (itr1 != None and itr2 != None):   # iterate through both the linked lists
            if (itr1.data != itr2.data):         # check if the corresponding data elements are same in every node; if not , they are not equal
                return 0
            else:
                itr1 = itr1.next
                itr2 = itr2.next
        return 1


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

        result = compare_lists(llist1.head, llist2.head)

        fptr.write(str(int(result)) + '\n')

    fptr.close()

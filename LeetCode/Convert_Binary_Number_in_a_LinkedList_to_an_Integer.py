# Problem name: Convert Binary Number in a Linked List to Integer
# Description: Given head which is a reference node to a singly-linked list.
# The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = ""
        curr = head
        while (curr):
            s += str(curr.val)
            curr = curr.next

        integer = int(s, 2)
        return integer


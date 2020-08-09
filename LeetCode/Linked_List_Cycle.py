# Problem name; Linked list cycle
# Description: Given a linked list, determine if it has a cycle in it.
#Strategy: as you traverse through a linked list, store the address values in a set, if you encounter a node, whose address is already in the list, return true

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        address = set()
        curr = head
        flag = 0
        while (curr != None):
            if (hex(id(curr)) not in address):
                address.add(hex(id(curr)))
                curr = curr.next
            else:
                flag = 1
                return True
        if (flag == 0):
            return False


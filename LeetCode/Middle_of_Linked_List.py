# Problem name: Middle of the Linked List
# Description: Given a non-empty, singly linked list with head node head, return a middle node of linked list.
# If there are two middle nodes, return the second middle node.
# Strategy: Traverse through the linked list and get the length, then find the pos of the node, to be returned


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 0
        curr = head
        while (curr != None):
            length += 1
            curr = curr.next
        if (length % 2 != 0):
            pos = (length + 1) // 2
        else:
            pos = (length // 2) + 1
        count = 0
        curr = head
        while (curr != None):
            count += 1
            if (count == pos):
                return curr
            else:

                curr = curr.next


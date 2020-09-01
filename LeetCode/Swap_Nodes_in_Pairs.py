#Problem name: Swap Nodes in Pairs
# Description: Given a linked list, swap every two adjacent nodes and return its head.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        temp = head
        while (temp is not None and temp.next is not None):
            t = temp.val
            temp.val = temp.next.val
            temp.next.val = t
            temp = temp.next.next
        return head




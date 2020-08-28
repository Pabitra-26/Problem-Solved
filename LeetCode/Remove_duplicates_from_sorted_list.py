# Problem name: Remove Duplicates from Sorted List
# Description: Given a sorted linked list, delete all duplicates such that each element appear only once.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        prev = head
        if (head is None):
            return
        while (curr.next is not None):
            prev = curr
            curr = curr.next
            if (prev.val == curr.val):
                prev.next = curr.next
                curr = prev
            else:
                continue
        if (prev.val == curr.val):
            prev.next = None

        return head
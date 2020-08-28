# Problem name: Remove Nth Node From End of List
# Description: Given a linked list, remove the n-th node from the end of list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count = 0
        curr = head
        while (curr):
            count += 1
            curr = curr.next
        if (count == n):
            head = head.next
            return head
        pos = count - n + 1
        if (count == 1):
            head = None
            return head
        curr = head
        prev = head
        count = 0

        while (count < pos - 1):
            count += 1
            prev = curr
            curr = curr.next
        prev.next = curr.next

        return head

# Problem name: Rotate List
# Description: Given a linked list, rotate the list to the right by k places, where k is non-negative.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if (head is None):
            return
        if (k == 0):
            return head

        count = 0
        curr = head
        while (curr is not None):
            count += 1
            curr = curr.next
        if (count == 1 and k > 1):
            return head

        if (k > count):
            k = k % count
        if (k == 0):
            return head

        if (count == k):
            return head
        pos = count - k

        count = 0
        curr = head
        prev = head
        while (count != pos):
            count += 1
            prev = curr
            curr = curr.next
        temp = curr
        prev.next = None
        prev = curr
        while (curr is not None):
            prev = curr
            curr = curr.next
        prev.next = head
        head = temp
        return head
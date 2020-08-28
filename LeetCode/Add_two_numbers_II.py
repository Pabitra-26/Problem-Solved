# Problem name: Add Two Numbers II
# Description: You are given two non-empty linked lists representing two non-negative integers.
# The most significant digit comes first and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = ""
        curr = l1
        while (curr is not None):
            s1 += str(curr.val)
            curr = curr.next
        s1 = int(s1)
        s2 = ""
        curr = l2
        while (curr is not None):
            s2 += str(curr.val)
            curr = curr.next
        s2 = int(s2)
        s1 += s2
        s1 = str(s1)
        head = None
        i = 1
        while (i < len(s1) + 1):
            if (head == None):
                head = ListNode(int(s1[-i]))
            else:
                node = ListNode(int(s1[-i]))
                node.next = head
                head = node
            i += 1
        return head



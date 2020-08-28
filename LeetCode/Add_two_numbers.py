# Problem name: Add two numbers
# Description: You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ""
        curr = l1
        while (curr):
            num1 += str(curr.val)
            curr = curr.next
        num1 = int(num1[::-1])
        num2 = ""
        curr = l2
        while (curr):
            num2 += str(curr.val)
            curr = curr.next
        num2 = int(num2[::-1])
        num = num1 + num2
        num = str(num)

        head = None
        i = 0
        while (i < len(num)):
            if (head == None):
                head = ListNode(int(num[i]))
            else:
                node = ListNode(int(num[i]))
                node.next = head
                head = node
            i += 1
        return head

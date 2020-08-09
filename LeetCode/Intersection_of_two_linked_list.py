# Problem name: Intersection of two linked list
# Description: Write a program to find the node at which the intersection of two singly linked lists begins.
#Strategy: store the addresses of list 1 in a set, while traversing through the second list, keep checking whether its address is in set, if yes, then return that node


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        set1 = set()
        curr = headA
        while (curr != None):
            if (hex(id(curr)) not in set1):
                set1.add(hex(id(curr)))
                curr = curr.next
        curr = headB
        while (curr != None):
            if (hex(id(curr)) in set1):
                return curr
            else:
                curr = curr.next




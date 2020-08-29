# Problem name: Linked List Cycle II
# Description: Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to.
# If pos is -1, then there is no cycle in the linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        table={}
        curr=head
        i=0
        m=0
        while(curr is not None):
            if(curr in table):
                m=1
                return curr
            else:
                table[curr]=1
                curr=curr.next
        if(m==0):
            return None
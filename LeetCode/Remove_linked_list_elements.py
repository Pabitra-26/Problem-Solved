# Problem name: Remove Linked List Elements
# Description: Remove all elements from a linked list of integers that have value val.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if(head is None):
            return None
        if(head.next==None and val==head.val):
            return None
        if(head.val==val):
            while(head is not None):
                if(head.val==val):
                    head=head.next
                else:
                    break
        if(head is None):
            return None
        curr=head
        prev=None
        while(curr is not None):
            if(curr.val==val):
                prev.next=curr.next
                curr=curr.next
            else:
                prev=curr
                curr=curr.next
        return head
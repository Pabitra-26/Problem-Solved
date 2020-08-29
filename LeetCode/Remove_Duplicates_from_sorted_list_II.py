# Problem name: Remove Duplicates from Sorted List II
# Description: Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
# Return the linked list sorted as well.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if(head is None):
            return None
        table={}
        curr=head
        while(curr is not None):
            if(curr.val in table):
                table[curr.val]+=1
            else:
                table[curr.val]=1
            curr=curr.next
        li=list(table.keys())
        li.sort()
        h=None
        i=0
        while(i<len(li)):
            if(table[li[i]]>1):
                i+=1
            else:
                node=ListNode(li[i])
                if(h is None):
                    h=node
                    curr=h
                else:
                    curr.next=node
                    curr=curr.next
                i+=1
        return h
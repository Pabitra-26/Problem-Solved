# Problem name: Find the Duplicate Number
# Description: Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        table={}
        for i in nums:
            if(i in table):
                return i
            else:
                table[i]=1
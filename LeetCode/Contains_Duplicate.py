# problem name: Contains Duplicate
# Description: Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        table={}
        flag=0
        for i in nums:
            if(i in table):
                flag=1
            elif(i not in table):
                table[i]=1
        if(flag==0):
            return False
        else:
            return True
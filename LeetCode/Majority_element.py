# Problem name: Majority Element
# Description: Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s=list(set(nums))
        n=len(nums)//2
        for i in s:
            if(nums.count(i)>n):
                return i
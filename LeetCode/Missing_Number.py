# Problem name: Missing Number
# Description: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        x=0
        for i in range(0,n+1):
            x^=i
        for i in nums:
            x^=i
        return x
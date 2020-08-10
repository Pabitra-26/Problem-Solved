# Problem name: Number of Good Pairs
# Description: Given an array of integers nums.
# A pair (i,j) is called good if nums[i] == nums[j] and i < j. Return the number of good pairs.


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i<j and nums[i]==nums[j]):
                    count+=1
        return count
# Problem name: Two Sum
# Description:Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Strategy: use two loops and iterate through the array, until you get the target, then break and append the index values to a list and return it

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        li=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    li.append(i)
                    li.append(j)
                    break
        return li
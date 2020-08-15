# Problem name: Maximum Product of Two Elements in an Array
# Description: Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                m = (nums[i] - 1) * (nums[j] - 1)
                if (m > maximum):
                    maximum = m
        return maximum

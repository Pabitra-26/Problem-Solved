# Problem name: Maximum subarray
# Description: Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
# Strategy: Dynamic programming

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        curr_max = nums[0]
        for i in range(1, len(nums)):
            curr_max = max(nums[i], nums[i] + curr_max)
            max_so_far = max(max_so_far, curr_max)
        return max_so_far

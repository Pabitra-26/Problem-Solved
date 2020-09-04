# Problem name: Remove Duplicates from Sorted Array
# Description: Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        count = 1
        m = len(nums)
        while (i < m - 1):
            if (nums[i] == nums[i + 1]):
                nums.pop(i + 1)
                m -= 1

            else:
                count += 1
                i += 1
        return count
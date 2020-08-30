# Problem name: Next Greater Element I
# Description: You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
# Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
# If it does not exist, output -1 for this number.


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        li = []
        for i in nums1:
            m = nums2.index(i)
            s = nums2[m + 1:]
            flag = 0
            for j in s:
                if (j > i):
                    li.append(j)
                    flag = 1
                    break
            if (flag == 0):
                li.append(-1)
        return li



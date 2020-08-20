#Problem name: Single number
# Description: Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Strategy: do xor of all elements, the final value will be that of the element occurring only once


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x=0
        for i in nums:
            x^=i
        return x
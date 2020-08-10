#Problem name: XOR operation in an array
# Description: Given an integer n and an integer start.
# Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.
# Return the bitwise XOR of all elements of nums.

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        li=[]
        for i in range(n):
            li.append(start+(2*i))
        xor=li[0]
        for i in range(1,n):
            xor^=li[i]
        return xor



# Problem name: Power of 2
# Description: Given an integer, write a function to determine if it is a power of two.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n == 0):
            return False
        elif (n & (n - 1) == 0):
            return True
        else:
            return False

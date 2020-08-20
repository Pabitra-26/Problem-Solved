# Problem name: Power of Four
# Description: Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if(num!=0 and (num&(num-1))==0 and (num&0xAAAAAAAA)==0):
            return True
        else:
            return False
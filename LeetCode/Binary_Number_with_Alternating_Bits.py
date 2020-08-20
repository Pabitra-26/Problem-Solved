# Problem name: Binary Number with Alternating Bits
# Description: Given a positive integer, check whether it has alternating bits:
# namely, if two adjacent bits will always have different values.


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b=0
        n=bin(n)
        n=n[2:]
        n=list(n)
        for i in range(len(n)-1):
            if(n[i]==n[i+1]):
                b=1
                return False
        if(b==0):
            return True
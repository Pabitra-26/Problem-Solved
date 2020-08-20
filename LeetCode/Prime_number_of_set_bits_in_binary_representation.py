# Problem name: Prime Number of Set Bits in Binary Representation
# Description: Given two integers L and R, find the count of numbers in the range [L, R] (inclusive)
# having a prime number of set bits in their binary representation.


class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        count=0
        for i in range(L,R+1):
            m=bin(i)
            m=m[2:]
            m=list(m)
            c=m.count('1')

            if(c==1):
                continue
            else:
                b=0
                for j in range(2,c):
                    if(c%j==0):
                        b=1
                if(b==0):
                    count+=1
        return count
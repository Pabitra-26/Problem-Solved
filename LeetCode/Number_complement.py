# Problem name: Number complement
# Description: Given a positive integer num, output its complement number.
# The complement strategy is to flip the bits of its binary representation.

class Solution:
    def findComplement(self, num: int) -> int:
        n=bin(num)
        n=n[2:]
        n=list(n)
        for i in range(len(n)):
            if(n[i]=='0'):
                n[i]="1"
            else:
                n[i]="0"
        m="".join(n)
        return(int(m,2))


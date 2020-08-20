# Problem name: Counting Bits
# Description: Given a non negative integer number num.
# For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

class Solution:
    def countBits(self, num: int) -> List[int]:
        li=[]
        for i in range(0,num+1):
            count=0
            while(i):
                count+=i&1
                i>>=1
            li.append(count)
        return li
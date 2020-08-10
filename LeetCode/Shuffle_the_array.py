# Problem name: Shuffle the Array
# Description: Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].
#Strategy: slicing and indexing in python

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1=nums[:n]
        l2=nums[n:]
        li=[]
        for i in range(n):
            li.append(l1[i])
            li.append(l2[i])
        return li

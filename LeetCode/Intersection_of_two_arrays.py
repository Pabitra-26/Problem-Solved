# Problem name: Intersection of Two Arrays
# Description: Given two arrays, write a function to compute their intersection.
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table={}
        for i in nums1:
            if i not in table:
                table[i]=1
            elif i in table:
                table[i]+=1
        li=[]
        for i in list(set(nums2)):
            if(i in table):
                li.append(i)
        return li
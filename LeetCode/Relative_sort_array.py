# Problem name: Relative Sort Array
# Description: Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
# Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort()
        li=[]
        for i in arr2:
            for j in arr1:
                if(i==j):
                    li.append(i)
        s=set(arr1)
        s1=set(li)
        s2=s-s1
        s2=list(s2)
        s2.sort()
        for i in s2:
            for j in arr1:
                if(i==j):
                    li.append(i)
        return li

# Problem name: Squares of a Sorted Array
# Description: Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        li=[]
        for i in A:
            li.append(i**2)
        li.sort()
        return li
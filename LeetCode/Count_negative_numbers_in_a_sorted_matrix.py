#Problem name:Count Negative Numbers in a Sorted Matrix
# Description: Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.
# Return the number of negative numbers in grid.

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for i in grid:
            for j in i:
                if(j<0):
                    count+=1
        return count
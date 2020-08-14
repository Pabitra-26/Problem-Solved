# Problem name:Cells with Odd Values in a Matrix
# Description:Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci].
# For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.
# Return the number of cells with odd values in the matrix after applying the increment to all indices.


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        li = [[0 for i in range(m)] for j in range(n)]
        for i in indices:
            row = i[0]
            col = i[1]
            for k in range(len(li[row])):
                li[row][k] += 1
            for k in range(len(li)):
                li[k][col] += 1
        odd = 0
        for i in li:
            for j in i:
                if (j % 2 == 1):
                    odd += 1
        return odd

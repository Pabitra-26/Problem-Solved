# Problem name: Matrix Diagonal Sum
# Description: Given a square matrix mat, return the sum of the matrix diagonals.
#
# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s=0
        if(len(mat))==1:
            if(len(mat[0])==1):
                return mat[0][0]
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if(i==j):
                    s+=mat[i][j]
                    s+=mat[i][len(mat[i])-j-1]
        if(len(mat)%2!=0):
            n=len(mat)//2
            s-=mat[n][n]
        return s
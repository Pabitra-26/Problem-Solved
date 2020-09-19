# Problem name: Unique Binary Search Trees
# Description: Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

class Solution:
    def fact(self, n):
        if (n == 0):
            return 1
        else:
            return n * self.fact(n - 1)

    def numTrees(self, n: int) -> int:
        num = 2 * n
        den_1 = n + 1
        den_2 = n
        return self.fact(num) // (self.fact(den_1) * self.fact(den_2))
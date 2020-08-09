# Problem name: Hamming Distance
# Description:The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, calculate the Hamming distance.



class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return (bin(x ^ y).count('1'))

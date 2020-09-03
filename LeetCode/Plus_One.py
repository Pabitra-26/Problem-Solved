# Problem name: Plus One
# Description: Given a non-empty array of digits representing a non-negative integer, increment one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in digits:
            s += str(i)
        s = int(s)
        s += 1
        s = str(s)
        li = []
        for i in s:
            li.append(int(i))
        return li

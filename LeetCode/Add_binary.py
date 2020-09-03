# Problem name: Add Binary
# Description: Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=int(a,2)
        b=int(b,2)
        s=a+b
        s=bin(s)
        s=s[2:]
        return s
# Problem name: Reverse Integer
# Description: Given a 32-bit signed integer, reverse digits of an integer.
# Strategy: use strings

class Solution:
    def reverse(self, x: int) -> int:
        y = str(x)
        if (y[0] == "-"):
            a = int("-" + y[-1:0:-1])
            if (a >= -2147483648 and a <= 2147483647):
                return a
            else:
                return 0
        else:
            a = int(y[::-1])
            if (a >= -2147483648 and a <= 2147483647):
                return a
            else:
                return 0

"""Problem name: Divide Two Integers
Description: Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero, which means losing its fractional part.
 For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
 Strategy: Keep the range of INTEGER value of a 32-bit machine"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        m = int(dividend / divisor)
        if (m > 2147483647):
            return 2147483647
        elif (m < -2147483648):
            return -2147483648
        else:
            return m

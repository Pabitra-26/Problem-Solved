# problem name: Split a String in Balanced Strings
# Description: Balanced strings are those who have equal quantity of 'L' and 'R' characters.
# Given a balanced string s split it in the maximum amount of balanced strings.
# Return the maximum amount of splitted balanced strings.#


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        res = 0
        for i in s:
            if (i == "L"):
                count += 1
            else:
                count -= 1
            if (count == 0):
                res += 1
        return res

# Problem name: Minimum Add to Make Parentheses Valid
# Description: Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.
#
# Formally, a parentheses string is valid if and only if:
#
# It is the empty string, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        count = 0
        i = 0
        s = []
        while (i < len(S)):
            p = S[i]
            if (p == '('):
                count += 1
                s.append(p)
            else:
                if (s == []):
                    count += 1
                else:
                    t = s.pop()
                    if (not (t == '(' and p == ')')):
                        count += 1
                    else:
                        count -= 1
            i += 1
        return count


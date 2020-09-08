# Problem name: Reverse Substrings Between Each Pair of Parentheses
# Description: You are given a string s that consists of lower case English letters and brackets.
# Reverse the strings in each pair of matching parentheses, starting from the innermost one.
# Your result should not contain any brackets.

class Solution:
    def reverseParentheses(self, s: str) -> str:
        word = ""
        m = len(s)
        stack = []
        for i in range(m):
            if (s[i] == '('):
                stack.append(i)
            elif (s[i] == ')'):
                temp = s[stack[-1]:i + 1]
                s = s[:stack[-1]] + temp[::-1] + s[i + 1:]
                del stack[-1]
        for i in s:
            if (i != '(' and i != ')'):
                word += i
        return word

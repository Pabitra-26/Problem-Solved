# Problem name: Valid Parentheses
# Description: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution:
    def match(self, t1, t2):
        if (t1 == '(' and t2 == ')'):
            return True
        elif (t1 == '[' and t2 == ']'):
            return True
        elif (t1 == '{' and t2 == '}'):
            return True
        else:
            return False

    def isValid(self, s: str) -> bool:
        stack = []
        index = 0
        is_balanced = True
        while (index < len(s) and is_balanced):
            p = s[index]
            if (p in "({["):
                stack.append(p)
            else:
                if (stack == []):
                    is_balanced = False
                else:
                    top = stack.pop()
                    if (not self.match(top, p)):
                        is_balanced = False
            index += 1
        if (is_balanced and stack == []):
            return True
        else:
            return False
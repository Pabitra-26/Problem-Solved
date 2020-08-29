# Problem name: Remove All Adjacent Duplicates In String
# Description: Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
#
# We repeatedly make duplicate removals on S until we no longer can.
#
# Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.


class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        top = 0
        for i in S:
            if (top == 0):
                stack.append(i)
                top += 1
            else:
                if (i == stack[top - 1]):
                    stack.pop()
                    top -= 1
                else:
                    stack.append(i)
                    top += 1

        s = "".join(stack)
        return s





# Problem name: Baseball Game
# Description: You're now a baseball game point recorder.
# Given a list of strings, each string can be one of the 4 following types:
# Integer (one round's score): Directly represents the number of points you get in this round.
# "+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
# "D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
# "C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
# Each round's operation is permanent and could have an impact on the round before and the round after.
# You need to return the sum of the points you could get in all the rounds.


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        li = []
        top = -1
        final = 0
        for i in ops:
            if (i == "C"):
                s = li.pop()
                final -= s
                top -= 1
            elif (i == "D"):
                s = li[top]
                final += (s * 2)
                li.append(2 * s)
                top += 1

            elif (i == "+"):
                s1 = li[top]
                s2 = li[top - 1]
                final += (s1 + s2)
                li.append(s1 + s2)
                top += 1
            else:
                li.append(int(i))
                top += 1
                final += int(i)
        return final
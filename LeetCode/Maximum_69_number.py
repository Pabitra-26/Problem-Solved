# Problem name: Maximum 69 Number
# Description: Given a positive integer num consisting only of digits 6 and 9.
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

class Solution:
    def maximum69Number(self, num: int) -> int:
        num = str(num)
        num = list(num)

        for i in range(len(num)):
            if (num[i] == "6"):
                num[i] = "9"
                break
        m = "".join(num)
        m = int(m)
        return m
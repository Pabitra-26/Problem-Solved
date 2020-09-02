# Problem name: Reverse Only Letters
# Description: Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

import string


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        str1 = ""
        p = string.punctuation + string.digits
        for i in S:
            if (i in p):
                continue
            else:
                str1 += i

        str1 = "".join(str1)
        str1 = str1[::-1]
        result = ""
        i = 0
        j = 0
        while (i < len(S)):
            if (S[i] not in p):
                result += str1[j]
                j += 1
                i += 1
            else:
                result += S[i]
                i += 1
        return result
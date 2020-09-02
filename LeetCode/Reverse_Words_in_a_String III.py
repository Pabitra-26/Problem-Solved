# Problem name: Reverse Words in a String III
# Description: Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        for i in range(len(s)):
            s[i] = s[i][::-1]
        s = " ".join(s)
        return s

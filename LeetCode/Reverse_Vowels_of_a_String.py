# Problem name: Reverse Vowels of a String
# Description: Write a function that takes a string as input and reverse only the vowels of a string.


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel=""
        consonant=""
        for i in s:
            if i in "aeiouAEIOU":
                vowel+=i
            else:
                consonant+=i
        vowel=vowel[::-1]
        final=""
        i=0
        v=0
        c=0
        while(i<len(s)):
            if(s[i] in "aeiouAEIOU"):
                final+=vowel[v]
                v+=1
            else:
                final+=consonant[c]
                c+=1
            i+=1
        return final
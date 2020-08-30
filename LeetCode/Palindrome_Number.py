# Problem name: Palindrome Number
# Description: Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        s=list(s)
        length=len(s)
        if(length%2==0):
            s1=s[0:length//2]
            s2=s[length//2:]
            s2=s2[::-1]
            if(s1==s2):
                return True
            else:
                return False
        else:
            s1=s[0:length//2]
            s2=s[(length//2)+1:]
            s2=s2[::-1]
            if(s1==s2):
                return True
            else:
                return False
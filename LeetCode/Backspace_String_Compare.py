# Problem name: Backspace String Compare
# Description: Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
#
# Note that after backspacing an empty text, the text will continue empty.

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s=[]
        for i in S:
            if(i=='#'):
                if(s==[]):
                    continue
                s.pop()
            else:
                s.append(i)
        t=[]
        for i in T:
            if(i=='#'):
                if(t==[]):
                    continue
                t.pop()
            else:
                t.append(i)
        if(s==t):
            return True
        else:
            return False
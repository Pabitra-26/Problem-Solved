# Problem name: Ransom Note
# Description: Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
#
# Each letter in the magazine string can only be used once in your ransom note.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        table={}
        for i in magazine:
            if(i in table):
                table[i]+=1
            else:
                table[i]=1
        flag=0
        for i in ransomNote:
            if(i in table):
                if(table[i]==0):
                    flag=1
                else:
                    table[i]-=1
            else:
                flag=1
        if(flag==1):
            return False
        else:
            return True
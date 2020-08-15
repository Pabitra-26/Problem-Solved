# Problem name: Jewels and Stones
# Description: You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
# Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
# The letters in J are guaranteed distinct, and all characters in J and S are letters.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".
# Strategy; Use hashing for J and then check which elements of S are present in it

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        table={}
        for i in range(len(J)):
            if(J[i] in table):
                table[J[i]]+=1
            elif(J[i] not in table):
                table[J[i]]=1
        count=0
        for i in range(len(S)):
            if(S[i] in table):
                count+=1
        return count
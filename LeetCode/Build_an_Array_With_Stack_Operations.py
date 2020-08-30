# Problem name: Build an Array With Stack Operations
# Description: Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.
# Build the target array using the following operations:
# Push: Read a new element from the beginning list, and push it in the array.
# Pop: delete the last element of the array.
# If the target array is already built, stop reading more elements.
# You are guaranteed that the target array is strictly increasing, only containing numbers between 1 to n inclusive.
# Return the operations to build the target array.
# You are guaranteed that the answer is unique.

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        if(n==len(target)):
            return ["Push"]*n
        if(n>len(target)):
            li=[]
            l=[]
            target=set(target)
            for i in range(n):
                if(i+1 in target):
                    li.append("Push")
                    l.append(i+1)
                else:
                    if(l==list(target)):
                        return li
                    li.append("Push")
                    li.append("Pop")
            return li
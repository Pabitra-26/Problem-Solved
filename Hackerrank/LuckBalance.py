# Problem name: Luck Balance
"""Description: Lena is preparing for an important coding competition that is preceded by a number of sequential preliminary contests.
 Initially, her luck balance is 0. She believes in "saving luck", and wants to check her theory.
  Each contest is described by two integers,L[i] and T[i]:
1) L[i] is the amount of luck associated with a contest. If Lena wins the contest, her luck balance will decrease by ;
 L[i] if she loses it, her luck balance will increase by L[i] .
2) T[i] denotes the contest's importance rating. It's equal to 1 if the contest is important, and it's equal to 0 if it's unimportant.
If Lena loses no more than k important contests, what is the maximum amount of luck she can have after competing in all the preliminary contests? This value may be negative."""

# Strategy: count the number of important contest and find the no. of number of contests, she needs to win.
# Find the contests with minimum points(important contests she needs to win) and subtract this value from the sum of the rest.



import math
import os
import random
import re
import sys

def luckBalance(k, contests):
    count = 0               # to count the number of important contests
    c=[]                    # to store the points(L[i])
    li = []                 # to store the points of important contests
    for i in contests:
        if (i[1] == 1):
            count += 1
            li.append(i[0])
        c.append(i[0])
    k=count-k              # to get the no. of contests she has to win
    li.sort()
    l=[]                  # to store the once she will lose
    for i in range(k):
        l.append(li.pop(0))

    return sum(c)-(2*sum(l))            # since we are finding sum of c, it includes the one we need to subtract as well, therefore, subtrat twice of what we need to subtract from it




if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)
    print(result)

# fptr.write(str(result) + '\n')

# fptr.close()

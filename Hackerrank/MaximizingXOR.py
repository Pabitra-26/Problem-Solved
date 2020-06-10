# Problem name: Maximizing XOR
# Description: Given two integers, l and r, find the maximal value of a xor b, where a and b satisfy the following condition: l<=a<=b<=r
# Strategy: using for loop find the xor of every element with itself and all the elements in that range, then return the maximum value

import math
import os
import random
import re
import sys


def maximizingXor(l, r):
    li=[]
    for i in range(l,r+1):                       # first loop from l to r+1(so that r is included
        for j in range(l,r+1):                  # second loop
            li.append(i^j)                        # append all xor values in a list
    return max(li)                                # return the maximum value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()

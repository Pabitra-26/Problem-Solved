# Problem name: Recursive Digit Sum
""" Description: Given an integer "x", we need to find the super digit of the integer.
1. If x has only  digit, then its super digit is x.
2. Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x ."""
# Strategy: Use of recursion

import math
import os
import random
import re
import sys


def superDigit(n,k):
    li=[int(n[i]) for i in range(0,len(n))]            # n is of type-str, so we first convert every character in n to an integer and store it in a list
    s=sum(li)                                          # finding the sum of all elements in the list- this gives us the sum of the digits of n when n is taken once
    s*=k                                               # sum of digits of n , when n is taken k times
    if(s<10):                                          # final superDigit will be >0 and <10
        return s
    else:
        return superDigit(str(s),1)                    # recursion , remember to pass k=1, as no more repetition is required

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = nk[0]
    k = int(nk[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()

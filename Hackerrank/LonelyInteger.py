# Problem name: Lonely Integer
"""Description: You will be given an array of integers. All of the integers except one occur twice.
That one is unique in the array. Given an array of integers, find and print the unique element."""
# Strategy: for the unique elements in the arr, count the number of times they occur

import math
import os
import random
import re
import sys


def lonelyinteger(a):
    m=set(a)                        # to get unique elements
    for i in m:                     # count the number of times they occur in a
        if(a.count(i)==1):
            return i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()

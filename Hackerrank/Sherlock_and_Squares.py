# Problem name: Sherlock and Squares
# Description: Watson likes to challenge Sherlock's math ability. He will provide a starting and ending value describing a range of integers.
# Sherlock must determine the number of square integers within that range, inclusive of the endpoints.
# Strategy: use math.ceil to get the square root values (range)

import math
import os
import random
import re
import sys

def squares(a, b):
    c = math.ceil((a ** 0.5) / 1)        # square root of a
    d = math.ceil((b ** 0.5) / 1)        # square root of b
    li = []                              # to store the square values
    for i in range(c, d + 1):
        sq = i ** 2                       # find the square of all numbers between c and d and then check if they lie between the the given range
        if (sq >= a and sq <= b):
            li.append(str(sq))

    return len(li)                     # return the length , to tell the number of integers


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()

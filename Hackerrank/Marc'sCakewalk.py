# Problem name: Marc's Cakewalk
""" Description: Marc loves cupcakes, but he also likes to stay fit. Each cupcake has a calorie count, and Marc can walk a distance to expend those calories.
 If Marc has eaten j cupcakes so far, after eating a cupcake with c calories he must walk at least (2^j)*c miles to maintain his weight.
 Given the individual calorie counts for each of the cupcakes, determine the minimum number of miles Marc must walk to maintain his weight. Note that he can eat the cupcakes in any order.
 Strategy: Multiply the largest number with smallest power of two. Arrange the array of calories in descending order and multiply each with ascending powers of 2"""

import math
import os
import random
import re
import sys


def marcsCakewalk(calorie):
    calorie.sort(reverse=True)        # descending order
    s=0                               # to calculate sum
    for i in range(len(calorie)):
        s+=(calorie[i]*(2**i))         # multiply with increasing powers of 2
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()



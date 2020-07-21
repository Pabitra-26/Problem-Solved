# Problem name: Minimum Distances
# Description: We define the distance between two array values as the number of indices between the two values.
# Given a, find the minimum distance between any pair of equal elements in the array. If no such value exists, print -1 .
# Strategy: store the values which occeur twice in a list(say, l), find the difference of index values of each elements in l and store it in another list(say, li), return the min(li).

import math
import os
import random
import re
import sys

def minimumDistances(a):
    l = set()
    li = []
    for i in a:
        if (a.count(i) == 2):
            l.add(i)
    l = list(l)
    for i in l:
        m = a.index(i)
        a[m] = 0
        n = a.index(i)
        li.append(abs(m - n))
    if li == []:
        return -1
    return min(li)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()

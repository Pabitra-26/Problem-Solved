# Problem name: Service lane
""" Description: Calvin is driving his favorite vehicle on the 101 freeway.
 He notices that the check engine light of his vehicle is on, and he wants to service it immediately to avoid any risks.
Luckily, a service lane runs parallel to the highway. The service lane varies in width along its length.
You will be given an array of widths at points along the road (indices), then a list of the indices of entry and exit points.
Considering each entry and exit point pair, calculate the maximum size vehicle that can travel that segment of the service lane safely."""
# Strategy: use indexing and slicing in python

import math
import os
import random
import re
import sys


def serviceLane(n, cases,width):
    li=[]
    for i in cases:                  # in cases, entry and exit values will be given, those are start and stop-1 values in slicing
        m=width[i[0]:i[1]+1]
        li.append(min(m))           # find the minimum value, so that it can fit in all
    return li

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases, width)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

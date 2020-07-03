# Problem name: Picking Numbers
# Description: Given an array of integers, find and print the maximum number of integers you can select from the array such that the absolute difference between any two of the chosen integers is less than or equal to 1.
# Strategy: using two for loops, compare the values and then append it to a list if the difference is 1, after one round of inner for loop, append the len of list to another list

import math
import os
import random
import re
import sys

def pickingNumbers(a):
    a.sort()              # first the input list is sorted
    count = []            # for storing the lengths
    for i in set(a):      # set(a) to get unique elements
        li = []           # to append elements with difference of 1 between them
        for j in range(a.index(i), len(a)):
            if (a[j] == i or a[j] == i + 1):
                li.append(a[j])
        count.append(len(li))  
    return max(count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

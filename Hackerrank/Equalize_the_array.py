# Problem name: Equalize the Array
# Description: Karl has an array of integers. He wants to reduce the array until all remaining elements are equal.
# Determine the minimum number of elements to delete to reach his goal.
# Strategy: make use of dictionary and also, keep various cases in mind

import math
import os
import random
import re
import sys

def equalizeArray(arr):    # keep in mind, only one element with maximum count in arr, has to remain
    d = dict()             # to hold the no. of occurences of each number in arr
    count = 0              # to store the minimum no. of deletions required
    for i in arr:
        d[i] = arr.count(i)  # storing the count values in dictionary
    m = max(d.values())       # find the maximum count value
    if (m == 1):              # if all the elements occur only once
        return len(arr) - 1   # remove all elements except 1 and return that value
    else:
        for i in d.values():  # remove all those values whose count is less than m(don't remove, just increment the count value
            if (i < m):
                count += i
    d = list(d.values())
    n = d.count(m)
    if (n > 1):              # there might be more than 2 numbers with same m(have to remove all except one)
        count += (m * (n - 1))
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

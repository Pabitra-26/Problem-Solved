# Problem name: Minimum Absolute Difference in an Array
# Description: Consider an array of integers, arr=[arr[0],arr[1],...,arr[n-1]].
# We define the absolute difference between two elements,a[i] and a[j] (where i!=j), to be the absolute value of a[i]-a[j].
# Given an array of integers, find and print the minimum absolute difference between any two elements in the array.
# Strategy: use greedy algorithm, first sort the given arr and append the difference of two consecutive elements to another list, return the minimum value in that list.

import math
import os
import random
import re
import sys


def minimumAbsoluteDifference(arr):
    arr.sort()              # sort the given array
    li = []
    for i in range(len(arr) - 1):
        li.append(abs(arr[i] - arr[i + 1]))        # difference of two consecutive elements, append the difference in li
    return min(li)                                 # return the minimum value in li


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

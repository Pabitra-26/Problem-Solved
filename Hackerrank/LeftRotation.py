#Problem name: Left Rotation
#Description: Given an array of n integers and a number,d , perform d left rotations on the array. Then print the updated array as a single line of space-separated integers.
#Strategy: Make use of list slicing and indexing

import math
import os
import random
import re
import sys
if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])                                      # no of elements in the array

    d = int(nd[1])                                      # no of rotations to be performed

    a = list(map(int, input().rstrip().split()))
    m=a[:d]                                         # Since d<=n always, no special case is required
    k=a[d:]
    l=k+m
    for i in l:
        print(i, end=" ")

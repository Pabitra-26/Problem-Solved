# Problem name: Sequence Equation
# Description: Given a sequence of n integers, p(1), p(2),...,p(n) where each element is distinct and satisfies 1<=p(x)<=n.
# For each  where 1<=x<=n, find any integer y such that p(p(y))=x and print the value of y on a new line.
# Strategy: use the index method of lists

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    l=sorted(p)               # store the sorted values of original list in another list
    li=[]
    for i in l:
        n=p.index(i)+1        # since the index values start from 1 in the given question, we have to increment the index values by 1, every time we find it.
        m=p.index(n)+1
        li.append(m)           # append the y values in a new list and return that list
    return li

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

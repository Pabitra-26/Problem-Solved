# Problem name: The Coin Change Problem
# Description: You are working at the cash counter at a fun-fair, and you have different types of coins available to you in infinite quantities. The value of each coin is already given. Determine the number of ways of making change for a particular number of units using the given types of coins
# Strategy: Overlapping Subproblems

import math
import os
import random
import re
import sys

def getWays(n, c):
    m=len(c)
    table=[0 for i in range(0,n+1)]          # Initialize all table values as 0
    table[0]=1                               # Base case (If given value is 0)
    for i in range(0,m):                      # Pick all coins one by one and update the table[] values after the index greater than or equal to the value of the picked coin
        for j in range(c[i],n+1):
            table[j]+=table[j-c[i]]
    return table[n]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))



    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()



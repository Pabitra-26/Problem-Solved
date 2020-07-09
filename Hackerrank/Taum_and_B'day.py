# Problem name: Taum and B'day
""" Description: Taum is planning to celebrate the birthday of his friend, Diksha.
 There are two types of gifts that Diksha wants from Taum: one is black and the other is white.
To make her happy, Taum has to buy b black gifts and w white gifts.
The cost of each black gift is bc units.
The cost of every white gift is wc units.
The cost of converting each black gift into white gift or vice versa is z units.
Help Taum by deducing the minimum amount he needs to spend on Diksha's gifts."""
# Strategy: Using simple if-else


import math
import os
import random
import re
import sys


def taumBday(b, w, bc, wc, z):
    s=0
    m=bc+z
    if(m<wc):
        s+=(m*w)
    else:
        s+=(w*wc)
    n=wc+z
    if(n<bc):
        s+=(n*b)
    else:
        s+=(b*bc)
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()

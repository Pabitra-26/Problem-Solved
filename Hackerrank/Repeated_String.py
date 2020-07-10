# Problem name: Repeated String
# Description: Lilah has a string,s , of lowercase English letters that she repeated infinitely many times.
# Given an integer,n ,find and print the number of letter a's in the first n letters of Lilah's infinite string.
# Strategy: use slicing of string




import math
import os
import random
import re
import sys


def repeatedString(s, n):
    count=0
    count=s.count('a')*(n//len(s))
    count+=s[:(n%len(s))].count('a')
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

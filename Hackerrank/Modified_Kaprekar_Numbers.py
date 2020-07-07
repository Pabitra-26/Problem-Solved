# Problem name: Modified Kaprekar Numbers
# Description: A modified Kaprekar number is a positive whole number with a special property.
# If you square it, then split the number into two integers and sum those integers, you have the same value you started with.
# Strategy: string conversion and slicing

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    result=[]
    for i in range(p,q+1):
        if(i==1):                     # since square of 1, 2 and 3 are single digits, we can write separate cases for them
            result.append(str(i))
        elif(i==2 or i==3):
            continue
        else:
            m=i**2                    # find the square->convert it to string-> slicing->store last d(number of digits in i) in b and the rest in a
            m=str(m)
            a=m[:len(m)//2]
            a=int(a)
            b=m[len(m)//2:]
            b=int(b)
            c=a+b                     # convert a and b to integer and find their sum, compare the sum with i, if same then append it to result, else continue
            m=int(m)
            if(c==i):
                result.append(str(i))
    if(len(result)==0):
        print("INVALID RANGE")
    else:
        result=" ".join(result)
        print(result)

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)

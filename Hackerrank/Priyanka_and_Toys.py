# Problem name: Priyanka and Toys
"""Description: Priyanka works for an international toy company that ships by container.
Her task is to the determine the lowest cost way to combine her orders for shipping.
She has a list of item weights. The shipping company has a requirement that all items loaded in a container must weigh less than or equal to 4 units plus the weight of the minimum weight item.
All items meeting that requirement will be shipped in one container.
What is the smallest number of containers that can be contracted to ship the items based on the given list of weights?"""
# Strategy: First sort the array of weights, then use while and a for loop to get the no. of containers

import math
import os
import random
import re
import sys


def toys(w):
    count=0              # to count the no. of containers
    w.sort()             # sort the given array
    i=0                  # index values of w
    while(i<len(w)):
        m=w[i]           #store the initial value of a container in m
        m+=4             # since a container can store weights upto 4 + minimum weight in that container
        for j in w[i:]:  # use a for loop to iterate through the values in w
            if(j<=m):
                i+=1    # increment the index value(as it can be stored in the same container
            else:       # different container
                count+=1 #increment the no.of containers
                break
    return count+1     # return count+1 to get the actual number of containers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()

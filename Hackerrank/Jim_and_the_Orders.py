# Problem name: Jim and the Orders
"""Description: Jim's Burgers has a line of hungry customers. Orders vary in the time it takes to prepare them.
 Determine the order the customers receive their orders. Start by numbering each of the customers from 1 to n, front of the line to the back.
  You will then be given an order number and a preparation time for each customer.
The time of delivery is calculated as the sum of the order number and the preparation time.
 If two orders are delivered at the same time, assume they are delivered in ascending customer number order."""
 # Strategy: add the order and prep time and store the values in a list. Copy this to another list(shallow copy) and sort the copied list.
# Then using the values in the sorted list and the index method of lists, find the final order in which customers get food.


import math
import os
import random
import re
import sys


def jimOrders(orders):
    li = []                     # store the sum of order and prep
    for i in orders:
        li.append(i[0] + i[1])
    m = []              # to store the final order in which they receive food
    l = []
    l = li.copy()              # shallow copy
    l.sort()                # sort it
    for i in l:
        n = li.index(i) + 1          # find the index values from li
        li[n - 1] = 0                 # since there might be same values: make the values of those index 0, whose ndex values have already been appended in m
        m.append(n)
    return m


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

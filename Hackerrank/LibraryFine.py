# Problem name: Library Fine
"""Description: Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:
If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine=0)
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine=15*(number of days late) hackos.
If the book is returned after the expected return month but still within the same calendar year as the expected return date, fine= 500*(number of months late) hackos .
If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10,000 hackos ."""
# Strategy: if-elif-else(nested)

import math
import os
import random
import re
import sys


# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    if (y1 < y2):                             # first check if the years are the same
        return 0
    elif (y1 == y2):
        if (m1 < m2):                         # then check if the months are same
            return 0
        elif (m1 == m2):
            if (d1 <= d2):                    # then check if the days are same
                return 0
            else:
                return 15 * (d1 - d2)
        else:
            return 500 * (m1 - m2)
    else:
        return 10000


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d1M1Y1 = input().split()

    d1 = int(d1M1Y1[0])

    m1 = int(d1M1Y1[1])

    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()

    d2 = int(d2M2Y2[0])

    m2 = int(d2M2Y2[1])

    y2 = int(d2M2Y2[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()

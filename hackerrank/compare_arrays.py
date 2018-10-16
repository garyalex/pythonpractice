#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.


def compareTriplets(a_arr, b_arr):
    acount = 0
    bcount = 0
    for a, b in zip(a_arr, b_arr):
        acount += 1 if a > b else 0
        bcount += 1 if b > a else 0

    return list(acount, bcount)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

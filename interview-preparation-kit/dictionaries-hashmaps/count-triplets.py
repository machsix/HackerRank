#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    arrC = {} # count number of each integer
    arrN = {}
    arg = 0
    for i, val in enumerate(arr):
        arrP = 0
        if val%r == 0:
            pval = int(val/r)
            if pval in arrC:
                # count number of preceeding val%r
                arrP = arrC[pval]
                arg += arrN[pval]

        # create a counter
        if val in arrC:
            arrC[val] += 1
        else:
            arrC[val] = 1
        if val in arrN:
            arrN[val] += arrP
        else:
            arrN[val] = arrP
    return arg



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()

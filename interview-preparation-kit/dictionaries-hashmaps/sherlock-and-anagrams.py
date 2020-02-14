#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from itertools import combinations

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    arr = 0
    n = len(s)
    for i in range(1,n):
        substrs = Counter([''.join(sorted(s[j:j+i])) for j in range(n-i+1)])
        for k in substrs.values():
            if k > 1:
                arr += int(k*(k-1)/2)
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

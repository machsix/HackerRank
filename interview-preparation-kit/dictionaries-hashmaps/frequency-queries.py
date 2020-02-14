#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    item = defaultdict(int)
    c = defaultdict(int)
    r = []
    for i,j in queries:
        if i == 1 or i == 2:
            if j not in item or (j in item and item[j] == 0):
                if i == 1:
                    item[j] = 1
                    c[1] += 1
            else:
                c[item[j]] -= 1
                item[j] += 1 if i == 1 else -1
                if item[j] != 0:
                    c[item[j]] += 1
        else:
            if j in c:
                r.append(1 if c[j] > 0 else 0)
            else:
                r.append(0)
    return r



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

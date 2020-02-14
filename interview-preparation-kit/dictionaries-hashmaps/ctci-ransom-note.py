#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    words = set(magazine)
    dic = {i: 0 for i in words}
    for i in magazine:
        dic[i] += 1

    for i in note:
        if i not in dic:
            print("No")
            return
        elif dic[i] == 0:
            print("No")
            return
        else:
            dic[i] -= 1
    print("Yes")




if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

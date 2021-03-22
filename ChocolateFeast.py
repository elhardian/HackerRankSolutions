

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    choco = int(n/c)
    freeChoco = int(choco/m)
    wrappers = (choco%m) + freeChoco
    result = 0
    while wrappers >= m:
        additional = int(wrappers/m)
        result = result + additional
        print(additional)
        print(wrappers)
        print("--------------")
        wrappers = additional + wrappers%m
    return choco + freeChoco + result
if __name__ == '__main__':

    t = int(input())
    arrResult = []
    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)
        print(str(result) + '\n')


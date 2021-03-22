#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    distA = z - x
    result = []
    if z < x:
        distA = x - z
    distB = z - y
    if z < y:
        distB = y - z
    if distA == distB:
        return 'Mouse C'
    elif distA > distB:
        return 'Cat B'
    else:
        return 'Cat A'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()

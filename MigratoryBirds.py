#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    sumType = [0 for i in range(5)]
    for x in arr:
        sumType[x-1] += 1
    highest = 0
    highestType = 0
    for x in range(5):
        if sumType[x] > highest:
            highestType = x+1
            highest = sumType[x]
            
    return highestType

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

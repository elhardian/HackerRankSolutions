#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    result = [0,0]
    recordValue = scores[0]
    lowestValue = scores[0]
    for i in range(2,len(scores) + 1):
        if scores[i-1] > recordValue:
            result[0] += 1
            recordValue = scores[i-1]
        if scores[i-1] < lowestValue:
            result[1] += 1
            lowestValue = scores[i-1]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

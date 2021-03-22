#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    seaLevel = 0
    countValley = 0
    for x in path:
        if x == 'U':
            if seaLevel < 0 and seaLevel + 1 == 0:
                countValley += 1
            seaLevel += 1
        else:
            seaLevel -= 1
    return countValley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

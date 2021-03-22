#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    totalFlip = int(n/2)
    result = 0
    if int(p/2) > int(totalFlip / 2):
        result = totalFlip - int(p / 2)
    else:
        result = int(p/2)
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

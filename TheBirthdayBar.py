
import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    match = 0
    if len(s) == 1:
        if s[0] == d and m == 1:
             return 1
            
    if m > len(s):
        return match
    
    for x in range(len(s)-(m-1)):
        count = s[x]
        for y in range(1,m):
            count += s[y+x]
        if(count == d):
            match += 1
    return match
            
            

if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(result)


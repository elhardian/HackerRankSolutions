
import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    countValue = [0 for x in range(9)]
    for x in range(3):
        for y in range(3):
            countValue[s[x][y]-1] += 1
            
    movement = 0
    print(countValue)
    for x in range(9):
        if countValue[x] == 0 or countValue[x] > 1:
            switch = 0
            for y in range(x,9):
                if countValue[y] > 1 and countValue[x] == 0:
                    switch = y + 1
                    break
                elif countValue[y] == 0 and countValue[x] > 1:
                    switch = y + 1
                    break
            countValue[switch - 1] = 1
            countValue[x] = 1
            movement = movement + abs(switch - (x +1))
            print(abs(switch - (x +1)))
            print(switch)
            print(x+1)
            print('-----')
    print(countValue)
    return movement

if __name__ == '__main__':

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    print(str(result) + '\n')


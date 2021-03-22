import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    dayMonth = [31, 28, 31, 30, 31, 30, 31, 31];
    if year < 1918 :
        if year % 4 == 0:
            dayMonth[1] = 29
    elif year == 1918:
        return '26.09.1918'
    elif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        dayMonth[1] = 29
    day = 256 - sum(dayMonth)
    result = str(day) + '.09.' + str(year)
    return result

if __name__ == '__main__':

    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result + '\n')

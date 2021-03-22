#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen"]
    tensOf = ["twenty", "half"]
    toOrPast = "past"
    minutes = ""
    if( m == 0):
        return words[h-1] + " o' clock" 
    elif m > 30:
        toOrPast = "to"
        m = 60 - m
        h = h + 1
    if m < 20:
        minutes = words[m-1]
    elif m != 30:
        minutes = tensOf[int(m/10)-2] + " " + words[(m%10)-1]
    else:
        minutes = tensOf[int(m/10)-2]
    if m > 1 and m != 15 and m != 30:
        minutes = minutes + " " + "minutes"
    elif m == 1:
        minutes = minutes + " " + "minute"
    return minutes + " " + toOrPast + " " + words[h-1]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()


import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hour, minutes, sec = map(int, s[:-2].split(':'))
    if s[-2:] == "PM":
        if hour != 12:
            hour = hour + 12
    elif hour == 12:
        hour = 0
    result = ('%02d:%02d:%02d') % (hour, minutes, sec)
    print(result)
    return result
if __name__ == '__main__':

    s = input()

    result = timeConversion(s)



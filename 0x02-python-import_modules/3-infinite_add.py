#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        print('0')
    else:
        sum = 0
        for i in range(1, len(args)):
            sum += int(args[i])
        print("{:d}".format(sum))

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    # Write your code here
    max_area = 0
    for i in range(len(h)):
        cnt = 0
        for j in range(i, -1, -1):
            if h[j] >= h[i]:
                cnt += 1
            else:
                break
        for k in range(i+1, len(h)):
            if h[k] >= h[i]:
                cnt += 1
            else:
                break
        area = h[i] * cnt
        if area > max_area:
            max_area = area
    return max_area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()

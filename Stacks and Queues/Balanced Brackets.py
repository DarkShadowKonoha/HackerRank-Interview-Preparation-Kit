#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(string):
    # Write your code here
    s = []
    for char in string:
        if char in '({[':
            s.append(char)
        elif char == ')':
            if(not s or s[-1]!='('):
                return 'NO'
            s.pop()
        elif char == '}':
            if(not s or s[-1]!='{'):
                return 'NO'
            s.pop()
        elif char == ']':
            if(not s or s[-1]!='['):
                return 'NO'
            s.pop()
    
    if not s:
        return 'YES'
    else:
        return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    n = len(arr)
    primary = 0
    secondary = 0
    for i in range(n):
        primary += arr[i][i]
        secondary += arr[i][n-1-i]
    
    if primary >= secondary:
        result = primary - secondary    
    else:
        result = secondary - primary
        
    return result

# Driver code.
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

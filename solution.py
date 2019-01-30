#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr, n):
    primarySum = 0
    secondarySum = 0
    i = 0
    j = 0
    for i in range(n):
        primarySum += arr[i][j]
        j += 1
    i = 0
    j = 0
    for i in range(n):
        secondarySum += arr[i][n - j - 1]
        j += 1
    sumDifference = abs(primarySum - secondarySum)
    return sumDifference


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()

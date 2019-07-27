#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    plus=0
    minus = 0
    zero = 0
    for each in arr:
        if each>0:
            plus+=1
        if each<0:
            minus+=1
        if each==0:
            zero+=1
    l = len(arr)
    print('{:.6f}'.format(plus/(l)))
    print('{:.6f}'.format(minus/(l)))
    print('{:.6f}'.format(zero/(l)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

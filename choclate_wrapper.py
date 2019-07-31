#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n,c,m):    
    wrapper = n//c
    total_bars = n//c
    while wrapper>=m:
        temp = wrapper//m
        total_bars += temp
        wrapper = wrapper%m 
        wrapper+=temp
    return total_bars

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    k %= 26
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = lower.upper()
    key = dict(zip(lower, lower[k:] + lower[:k])) | dict(zip(upper, upper[k:] + upper[:k]))
    return s.translate(s.maketrans(key))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

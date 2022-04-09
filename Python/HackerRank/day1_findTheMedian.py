#https://www.hackerrank.com/challenges/flipping-the-matrix/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

# 생각보다 너무 간단한 문제였다.
def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix)//2
    ans = 0
    for i in range(n):
        for j in range(n):
            ans += max(matrix[i][j],matrix[i][-j-1],matrix[-i-1][j],matrix[-i-1][-j-1])
    
    return ans     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()






# Failure
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix)//2
    from itertools import chain
    from heapq import heapify
    
    outbound = list(set(chain(matrix[0],matrix[-1],matrix[:][0],matrix[:][-1])))
    heapify(outbound)
    
    inbound = []
    
    for i in range(1,n*2-1):
        for j in range(1,n*2-1):
            inbound.append(matrix[i][j])

    heapify(inbound)
    print(outbound,inbound)
    print(-n*2+1, -(n-1)**2)
    return sum(outbound[-n*2+1:]) + sum(inbound[-((n-1)**2):]

if __name__ == '__main__':)
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()

"""
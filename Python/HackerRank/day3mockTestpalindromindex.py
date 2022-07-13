#!/bin/python3

import math
import os
import random
import re
import sys

#https://hackerranksolution.in/palindromeindexalgo/

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def palindromeIndex(s):
    # Write your code here
    # for i in range(len(s)//2):
    #     if s[i] != s[-(i+1)]:
    #         newstr = s[:i] + s[i+1:] 
    #         if newstr[:] == newstr[::-1]:
    #             return i
    #         return -(i+1)+len(s)
    # return -1
    s = list(s)

    if s[::] == s[::-1]:
        return -1

    # 이렇게 다 저장을 하니까 정말 긴 문장에 대해서 런타임 에러가 나는 듯
    li = [s[1:]]
    for i in range(1,len(s)-1):
        li.append(s[:i]+s[i+1:])
    li.append(s[:-1])
    # print(li)
    # for i in range(len(s)):
    for i,l in enumerate(li):
        
        # if log: s.insert(*log.pop())
        # log.append((i,s.pop(i)))
        # print(s,log)
        if l[::] == l[::-1]:
            return i
        else:
            pass
    return -1

def othersolution():
    for _ in range(int(input())):
        s = input()
        a, b = 0, len(s)-1
        result = -1
        if a == b:
            print(-1)
        else:
            while a != b:
                if a == len(s)-1 or b == 0:
                    break
                if s[a] == s[b]:
                    a, b = a+1 , b-1
                else:
                    if s[a] == s[b-1] and s[a+1] == s[b-2]:
                        result = b
                        break
                    else :
                        result = a
                        break

        print(result)
# othersolution()
print(palindromeIndex(str(input())))
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input().strip())

#     for q_itr in range(q):
#         s = input()

#         result = palindromeIndex(s)

#         fptr.write(str(result) + '\n')

#     fptr.close()

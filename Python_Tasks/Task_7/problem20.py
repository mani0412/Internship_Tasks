# Super Reduced String
# https://www.hackerrank.com/challenges/reduced-string/problem
import math
import os
import random
import re
import sys

def superReducedString(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    result = ''.join(stack)

    if result == "":
        return "Empty String"
    else:
        return result

    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()

# Separate the Numbers
# https://www.hackerrank.com/challenges/separate-the-numbers/problem
import math
import os
import random
import re
import sys

def separateNumbers(s):
    # Write your code here
    if len(s) < 2 or s[0] == '0':
        print("NO")
        return

    for i in range(1, len(s) // 2 + 1):
        first = int(s[:i])
        current = first
        result = str(current)

        while len(result) < len(s):
            current += 1
            result += str(current)

        if result == s:
            print("YES", first)
            return

    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)

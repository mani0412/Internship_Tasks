# Piling Up!
# https://www.hackerrank.com/challenges/piling-up/problem
from collections import deque

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n = int(input())
        blocks = deque(map(int, input().split()))

        top = float('inf')
        possible = True

        while blocks:
            if blocks[0] >= blocks[-1]:
                cube = blocks.popleft()
            else:
                cube = blocks.pop()

            if cube > top:
                possible = False
                break
            top = cube

        if possible:
            print("Yes")
        else:
            print("No")

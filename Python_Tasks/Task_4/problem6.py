# Find the Runner-Up Score!
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

n = int(input())
arr = list(map(int, input().split()))
arr = list(set(arr))
arr.sort()
print(arr[-2])

# Write a Function
# https://www.hackerrank.com/challenges/write-a-function/problem
def is_leap(year):
    leap = False
    if year % 4 == 0:
        bool("True")
    elif year % 100 == 0:
        bool("False")
    elif year % 400 == 0:
        bool("True")    # Write your logic here
    
    return leap

year = int(input())

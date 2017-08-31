#!/bin/python

# https://www.hackerrank.com/challenges/the-birthday-bar/problem

import sys

def solve(n, s, d, m):
    # Complete this function
    cnt = 0 # how many arrays
    if n >= m:
        for i in range(0,n - m + 1):
            total = s[i]
            for j in range(i + 1, i + m ):
                total = total + s[j]
            if total == d:
                cnt += 1
    return cnt

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)

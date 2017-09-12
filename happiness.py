# https://www.hackerrank.com/challenges/no-idea?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=3-day-campaign


import sys
from collections import Counter

# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int,sys.stdin.readline().split())
arr = Counter(list(map(int,sys.stdin.readline().split())))
a = set(list(map(int,sys.stdin.readline().split())))
b = set(list(map(int,sys.stdin.readline().split())))
total = 0

for item, cnt in arr.items():
    if item in a:
        total = total + (1*cnt)
    if item in b:
        total = total +  + (-1 * cnt)
print total

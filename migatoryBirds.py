#!/bin/python
# https://www.hackerrank.com/challenges/migratory-birds?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
# Main thing is how to use sorted function

import sys
from collections import Counter

def migratoryBirds(n, ar):
    # Complete this function
    sorted_result = sorted(Counter(ar).most_common(), key=lambda x: (-x[1],x[0]))
    if len(sorted_result) > 0:
        return sorted_result[0][0]
    return 0
        

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = migratoryBirds(n, ar)
print(result)

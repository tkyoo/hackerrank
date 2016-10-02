#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

positive= 0
negative= 0
zero = 0

for element in arr:
    if element > 0:
        positive += 1
    elif element < 0:
        negative += 1
    else:
        zero += 1

print("%.6f" % (positive / float(n)))
print("%.6f" % (negative / float(n)))
print("%.6f" % (zero / float(n)))

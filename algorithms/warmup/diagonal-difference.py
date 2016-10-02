#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

rightDownDirection=0
leftDownDirection=0
i = 0
j = 0

while i < n:
    rightDownDirection += a[i][j]
    leftDownDirection += a[n-i-1][j]
    i += 1
    j += 1

print(abs(rightDownDirection - leftDownDirection))

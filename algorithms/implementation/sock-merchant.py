#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

d = dict()
cnt = 0

for e in c:
    if e in d:
        d[e] += 1
        if d[e] % 2 == 0:
            cnt += 1
    else:
        d[e] = 1

print(cnt)

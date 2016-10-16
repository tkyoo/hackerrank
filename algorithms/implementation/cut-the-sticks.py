#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

while True:
    Min = 999
    cnt = 0
    for e in arr:
        if e > 0:
            cnt += 1
            if Min > e:
                Min = e

    if cnt == 0:
        break;
    else:
        print(cnt)

    for index in range(len(arr)):
        arr[index] -= Min

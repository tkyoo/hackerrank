#!/bin/python3

import sys


x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

flag = x1 > x2

while True:
    if x1 == x2:
        print("YES")
        break
    else:
        if flag:
            if v1 >= v2:
                print("NO")
                break
            else:
                if x1 < x2:
                    print("NO")
                    break
        else:
            if v1 <= v2:
                print("NO")
                break
            else:
                if x1 > x2:
                    print("NO")
                    break
    x1 += v1
    x2 += v2


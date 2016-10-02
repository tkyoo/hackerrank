#!/bin/python3

import sys


n = int(input().strip())

for index in range(n):
    print( ("#"*(index+1)).rjust(n) )

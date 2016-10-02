#!/bin/python3

import sys


time = input().strip()

ampm = time[len(time)-2:]

hour=time[0:2]

if ampm == "PM":
    if hour != "12":
        hour = int(time[0:2]) + 12

    print(str(hour) + time[2:len(time)-2])
elif ampm == "AM":
    if hour == "12":
        hour = "00"
    print(str(hour) + time[2:len(time)-2])


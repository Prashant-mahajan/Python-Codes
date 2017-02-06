#!/bin/python3

import sys
import datetime

time = input().strip()
time = datetime.datetime.strptime(time, "%I:%M:%S%p")
#%H is the 24 hour clock, %I is the 12 hour clock and when using the 12 hour clock, %p qualifies if it is AM or PM
ans = datetime.datetime.strftime(time, "%H:%M:%S") 
print(ans)
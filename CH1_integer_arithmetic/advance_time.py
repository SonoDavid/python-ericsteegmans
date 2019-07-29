# Python function that takes a string and reads it as a time
# It also advances the time by one second
# It then prints the output as hh:mm:ss
#
# Author: Joachim David
# Date: June 2019

from datetime import time, timedelta

hours = int(input('Enter hours: '))
assert (0 <= hours < 24), 'Hours not within range [0-23]'
minutes = int(input('Enter minutes: '))
assert (0 <= minutes < 60), 'Minutes not within range [0-59]'
seconds = int(input('Enter seconds: '))
assert (0 <= seconds < 60), 'Seconds not within range [0-59]'

curtime = time(hour=hours, minute=minutes, second=seconds)

seconds += 1
if seconds >= 60:
    seconds %= 60
    minutes += 1
if minutes >= 60:
    minutes %= 60
    hours +=1
if hours >= 24:
    hours %= 24 

advtime = time(hour=hours, minute=minutes, second=seconds)

#advtime = curtime + timedelta(seconds=1)
print('Advanced time', advtime.isoformat())


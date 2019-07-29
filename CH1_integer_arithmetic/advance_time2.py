# Python function that takes a string and reads it as a time
# It also advances the time by one second
# It then prints the output as hh:mm:ss
#
# Author: Joachim David
# Date: June 2019

from datetime import time, timedelta

class MyTime:
    def __init__(self):
        self.mytime = self.input_time()

    def input_time(self):
        hours = int(input('Enter hours: '))
        assert hours in range(24), 'Hours not within range [0-23]'
        minutes = int(input('Enter minutes: '))
        assert minutes in range(60), 'Minutes not within range [0-59]'
        seconds = int(input('Enter seconds: '))
        assert seconds in range(60), 'Seconds not within range [0-59]'
        mytime = time(hour=hours, minute=minutes, second=seconds)
        return mytime

    def add_seconds(self, sec):
        print(self.mytime)
        seconds = self.mytime.second
        minutes = self.mytime.minute
        hours = self.mytime.hour
        seconds += sec
        if seconds >= 60:
            minutes += (seconds // 60)
            seconds %= 60
        if minutes >= 60:
            hours +=  (minutes // 60)
            minutes %= 60
        if hours >= 24:
            hours %= 24
        return time(hour=hours, minute=minutes, second=seconds)


enter_time = MyTime()

advtime = enter_time.add_seconds(1)

#advtime = curtime + timedelta(seconds=1)
print('Advanced time', advtime.isoformat())


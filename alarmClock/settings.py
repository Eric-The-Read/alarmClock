'''Contains variables which are used by the window elements in the alarm clock.'''
import os

clocks = []
dateFmt = ["%m/%d/%Y %I:%M:%S %p"]
dayList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
hourList = [str(i).zfill(2) for i in range(1,13)]
minuteList = [str(i).zfill(2) for i in range(1, 60)]
periodList = ['AM', 'PM']








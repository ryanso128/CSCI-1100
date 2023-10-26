# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 18:09:15 2022

@author: ryani
Asks user to input minutes, seconds, miles, and a target miles. Calculates
a Pace, Speed, and a time to run to target distance.

"""

minutes=input('Minutes ==> ')
print(minutes)
seconds=input('Seconds ==> ')
print(seconds)
miles=input('Miles ==> ')
print(miles)
target_miles=input('Target Miles ==> ')
print(target_miles)
print('\n', end='')
seconds_per_mile=(((float(minutes)*60)+float(seconds))/float(miles))
running_minutes=seconds_per_mile//60
running_seconds=seconds_per_mile%60
print('Pace is ', int(running_minutes), ' minutes and ', int(running_seconds), ' seconds per mile.', sep='')
speed=float(miles)/((float(minutes)+(float(seconds)/60)))*60
print('Speed is {:.2f} miles per hour.'.format(speed))
target=int(seconds_per_mile*float(target_miles))
target_minute=int(target/60)
target_seconds=int(target%60)
print('Time to run the target distance of {:.2f} miles is {} minutes and {} seconds.'.format(float(target_miles), target_minute, target_seconds))
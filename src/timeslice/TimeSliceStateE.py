'''
Created on Apr 9, 2014

@author: alexandermertens
'''
from enum import Enum

class TimeSliceStateE(Enum):
    inited    = 1
    running   = 2
    completed = 3
    cancelled = 4

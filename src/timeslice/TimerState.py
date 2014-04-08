'''
Created on Apr 4, 2014

@author: swym
'''
from enum import Enum

class TimerState(Enum):
    inited     = 1
    running    = 2
    halted     = 3
    terminated = 4
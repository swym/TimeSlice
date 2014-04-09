'''
Created on Apr 9, 2014

@author: alexandermertens
'''
from datetime import timedelta, datetime
from timeslice.TimeSliceStateE import TimeSliceStateE

class TimeSlice(object):
    '''
    classdocs
    '''
    def __init__(self, duration):
        '''
        Constructor
        '''
        self.__duration   = timedelta(minutes = duration)
        self.__startTime  = None
        
        self.__state = TimeSliceStateE.inited
        
    def start(self):
        if self.__state == TimeSliceStateE.inited:
            self.__startTime = datetime.now()
            self.__state     = TimeSliceStateE.running
            
    def cancel(self):
        if self.__state == TimeSliceStateE.running:
            self.__state = TimeSliceStateE.cancelled
            
    def getRemainingTime(self):
        if self.__state == TimeSliceStateE.inited:
            return self.__duration
        elif self.__state == TimeSliceStateE.running:
            return self.__startTime + self.__duration - datetime.now()
        else:
            #TimeSliceStateE.completed
            #TimeSliceStateE.cancelled
            return timedelta(seconds = 0)
        
    def __updateState(self):
        if self.__state == TimeSliceStateE.running:
            if not (self.__startTime + self.__duration) > datetime.now():
                self.__state = TimeSliceStateE.completed
        return self.__state
    
    def isInited(self):
        return self.__updateState() == TimeSliceStateE.inited
    
    def isRunning(self):
        return self.__updateState() == TimeSliceStateE.running
    
    def isCompleted(self):
        return self.__updateState() == TimeSliceStateE.completed
    
    def isCancelled(self):
        return self.__updateState() == TimeSliceStateE.cancelled    
    
        
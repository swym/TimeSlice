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
    def __init__(self, title, duration):
        '''
        Constructor
        '''
        self.__title = title
        self.__duration   = timedelta(seconds = duration)
        self.__startTime  = None
        self.__state = TimeSliceStateE.inited
        
    def start(self):
        self.__updateState()
        if self.__state == TimeSliceStateE.inited:
            self.__startTime = datetime.now()
            self.__state     = TimeSliceStateE.running
            
    def cancel(self):
        self.__updateState()
        if self.__state == TimeSliceStateE.running:
            self.__state = TimeSliceStateE.cancelled
            
    def getRemainingTime(self):
        if self.isInited():
            return self.__duration
        elif self.isRunning():
            return self.__startTime + self.__duration - datetime.now()
        else:
            #TimeSliceStateE.completed
            #TimeSliceStateE.cancelled
            return timedelta(seconds = 0)
        
    def __updateState(self):
        if self.__state == TimeSliceStateE.running:
            if (self.__startTime + self.__duration) <= datetime.now():
                self.__state = TimeSliceStateE.completed
        return self.__state
    
    def getDuration(self):
        return self.__duration
    
    def getTitle(self):
        return self.__title
    
    def isInited(self):
        return self.__updateState() == TimeSliceStateE.inited
    
    def isRunning(self):
        return self.__updateState() == TimeSliceStateE.running
    
    def isCompleted(self):
        return self.__updateState() == TimeSliceStateE.completed
    
    def isCancelled(self):
        return self.__updateState() == TimeSliceStateE.cancelled
    
    def __str__(self, *args, **kwargs):
        return ("title:"  + str(self.__title) +
                ",dur:"   + str(self.__duration) +
                ",state:" + str(self.__state))
       
    def __repr__(self, *args, **kwargs):
        return self.__str__()
        
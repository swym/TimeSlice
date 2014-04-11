'''
Created on Apr 9, 2014

@author: alexandermertens
'''
from datetime import timedelta, datetime
from timeslice.TimeSliceStateE import TimeSliceStateE
from timeslice.Interruptions import Interruptions

class TimeSlice(object):
    '''
    classdocs
    '''
    def __init__(self, title, duration):
        '''
        Constructor
        '''
        self._title      = title
        #self._duration   = timedelta(minutes = duration)
        # TODO: DEBUG: duration should be minutes.
        self._duration   = timedelta(seconds = duration)
        self._startTime  = None
        self._state      = TimeSliceStateE.inited

        self._external_interruptions = Interruptions()
        self._internal_interruptions = Interruptions()

    def start(self):
        self._update_state()
        if self._state == TimeSliceStateE.inited:
            self._startTime = self._my_now()
            self._state     = TimeSliceStateE.running
            
    def cancel(self):
        self._update_state()
        if self._state == TimeSliceStateE.running:
            self._state = TimeSliceStateE.cancelled
            
    def get_remaining_time(self):
        if self.is_inited():
            return self._duration
        elif self.is_running():
            return self._startTime + self._duration - self._my_now()
        else:
            #TimeSliceStateE.completed
            #TimeSliceStateE.cancelled
            return timedelta(seconds = 0)

    def _update_state(self):
        if self._state == TimeSliceStateE.running:
            if (self._startTime + self._duration) <= self._my_now():
                self._state = TimeSliceStateE.completed
        return self._state
    
    def get_duration(self):
        return self._duration
    
    def get_title(self):
        return self._title
    
    def _my_now(self):
        now = datetime.now()
        return timedelta(hours = now.hour, minutes =  now.minute, seconds = now.second)

    def inc_external_interruptions(self):
        if self._state == TimeSliceStateE.running:
            self._external_interruptions.inc()
 
    def get_external_interruptions(self):
        return self._external_interruptions.get()
    
    def inc_internal_interruptions(self):
        if self._state == TimeSliceStateE.running:
            self._internal_interruptions.inc()

    def get_internal_interruptions(self):
        return self._internal_interruptions.get()
    
    def is_inited(self):
        return self._update_state() == TimeSliceStateE.inited
    
    def is_running(self):
        return self._update_state() == TimeSliceStateE.running
    
    def is_completed(self):
        return self._update_state() == TimeSliceStateE.completed
    
    def is_cancelled(self):
        return self._update_state() == TimeSliceStateE.cancelled
    
    def __str__(self, *args, **kwargs):
        return ("title:"  + str(self._title) +
                ",dur:"   + str(self._duration) +
                ",state:" + str(self._state))
       
    def __repr__(self, *args, **kwargs):
        return self.__str__()
        
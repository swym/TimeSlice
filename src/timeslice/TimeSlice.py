'''
Created on Apr 9, 2014

@author: alexandermertens
'''
from datetime import timedelta, datetime
from timeslice.TimeSliceStateE import TimeSliceStateE
from timeslice.Interruptions import Interruptions
from threading import Thread
from util.observer.Subject import Subject
from time import sleep

class TimeSlice(Thread, Subject):

    '''
    classdocs
    '''
    def __init__(self, title, duration, quantification = 'm'):
        '''
        Constructor
        '''
        Subject.__init__(self)
        Thread.__init__(self)
        
        
        self._title      = title
        # TODO: DEBUG: duration should be minutes.
        if quantification == 's':
            self._duration = timedelta(seconds = duration)
        else: 
            self._duration = timedelta(minutes = duration)

        self._startTime  = None
        self._state      = TimeSliceStateE.inited

        self._external_interruptions = Interruptions()
        self._internal_interruptions = Interruptions()

    def run(self):
        if self.is_inited():
            self._startTime = self._my_now()
            self._state     = TimeSliceStateE.running
            self.notifyObservers(self._state)

            self._update_state()    
            while self.is_running():
                self._update_state()

            self.notifyObservers(self._state)

    def cancel(self):
        if self._state == TimeSliceStateE.running:
            self._state = TimeSliceStateE.cancelled
            
            
    def get_remaining_time(self):
        if self.is_inited():
            return self._duration
        elif self.is_running():
            return self._startTime + self._duration - self._my_now()
        else:
            #if self._state == TimeSliceStateE.completed
            #if self._state == TimeSliceStateE.cancelled
            return timedelta(seconds = 0)

    def _update_state(self):
        if  self.is_running() and \
           (self._startTime + self._duration) <= self._my_now():
                self._state = TimeSliceStateE.completed

    def _my_now(self):
        now = datetime.now()
        return timedelta(hours = now.hour, minutes =  now.minute, seconds = now.second)
 
    def get_duration(self):
        return self._duration
    
    def get_title(self):
        return self._title


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
        return self._state == TimeSliceStateE.inited
    
    def is_running(self):
        return self._state == TimeSliceStateE.running
    
    def is_completed(self):
        return self._state == TimeSliceStateE.completed
    
    def is_cancelled(self):
        return self._state  == TimeSliceStateE.cancelled
    
    
    def __str__(self, *args, **kwargs):
        return ("title:"  + str(self._title) +
                ",dur:"   + str(self._duration) +
                ",state:" + str(self._state))
       
    def __repr__(self, *args, **kwargs):
        return self.__str__()
        
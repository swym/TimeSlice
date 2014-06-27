'''
Created on Apr 9, 2014

@author: alexandermertens
'''
from timeslice.TimeSlice import TimeSlice
from datetime import datetime
#from timeslice.Interruptions import interruption
from collections import deque
from util.observer.Observer import Observer
from timeslice.TimeSliceStateE import TimeSliceStateE
from timeslice.Hookup import Hookup
from timeslice.Watchdog import Watchdog


class Session(Observer):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._timeslices = deque()
        
        ts = TimeSlice("productive", 25, 'm')
        ts.attachObserver(self)
        self._timeslices.append(ts)

        ts = TimeSlice("pause", 5, 'm')
        ts.attachObserver(self)        
        self._timeslices.append(ts)
        
        self._hookup = Hookup()
        
        self._watchdog = Watchdog(60)
        self._watchdog.attachObserver(self)
        self._watchdog.start()


    def start_current_timeslice(self):
        # TODO: search a more elegant solution with better exection handling
        if len(self._timeslices) > 0:
            self._timeslices[0].start()
            return self.is_current_timeslice_running()
        else: return False

    def cancel_current_timeslice(self):
        # TODO: search a more elegant solution with better exection handling
        if len(self._timeslices) > 0:
            self._timeslices[0].cancel()
            return self.is_current_timeslice_cancelled()
        else: return False
    
    def next_timeslice(self):
        if len(self._timeslices) > 0:            
            if(self.is_current_timeslice_completed() or
               self.is_current_timeslice_cancelled()):
                self._timeslices.popleft()

    def get_current_timeslice(self):
        # TODO: Only for debugging; Remove in further commits
        if len(self._timeslices) > 0:
            return self._timeslices[0]    
    
    def get_current_timeslice_title(self):
        if len(self._timeslices) > 0:
            return self._timeslices[0].get_title()
        else: return None
    
    def get_current_timeslice_duration(self):
        if len(self._timeslices) > 0:
            return self._timeslices[0].get_duration()
        else: return None
        
    def is_current_timeslice_inited(self):
        if len(self._timeslices) > 0:
            return self._timeslices[0].is_inited()
        else: return False
    
    def is_current_timeslice_running(self):
        if len(self._timeslices) > 0:
            return self._timeslices[0].is_running()
        else: return False
    
    def is_current_timeslice_completed(self):
        if len(self._timeslices) > 0:
            return self._timeslices[0].is_completed()
        else: return False
    
    def is_current_timeslice_cancelled(self):
        if len(self._timeslices) > 0:
            return self._timeslices[0].is_cancelled()
        else: return False
    
    def has_timeslices(self):
        return len(self._timeslices) > 0
    
    def get_timeslice_count(self):
        return len(self._timeslices)
    
    def get_current_time(self):
        return datetime.now()

    def inc_current_timeslice_external_interruptions(self):
        if len(self._timeslices) > 0:
            self._timeslices[0].inc_external_interruptions()
        else: return False
        
    def get_current_timeslice_external_interruptions(self):
        if len(self._timeslices) > 0:
            return self._timeslices[0].get_external_interruptions()
        else: return None

    def inc_current_timeslice_internal_interruptions(self):
        if len(self._timeslices) > 0:
            self._timeslices[0].inc_internal_interruptions()
        else: return False

    def get_current_timeslice_internal_interruptions(self):
        if len(self._timeslices) > 0:
            return self._timeslices[0].get_internal_interruptions()
        else: return None   

    def shutdown(self):
        self._watchdog.stop()
        for ts in self._timeslices:
            ts.cancel()

    def update(self, subject, param):
        
        if isinstance(subject, TimeSlice):
            if(param == TimeSliceStateE.running):
                self._hookup.hookup_start(subject)
            elif(param == TimeSliceStateE.completed):
                self._hookup.hookup_complete(subject)
            elif(param == TimeSliceStateE.cancelled):
                self._hookup.hookup_cancelled(subject)
            elif(param == "interrupted"):
                self._hookup.hookup_interrupted(subject)
            
            self._watchdog.reset()

        if isinstance(subject, Watchdog):
            if param == "fired":
                if self.get_current_timeslice() == None or \
                   not self.is_current_timeslice_running():
                    self._hookup.hookup_watchdog_fired()
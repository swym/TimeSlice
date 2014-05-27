'''
Created on Apr 9, 2014

@author: alexandermertens
'''
from timeslice.TimeSlice import TimeSlice
from datetime import datetime
#from timeslice.Interruptions import interruption
from collections import deque
from util.observer.Observer import Observer
from os.path import os


class Session(Observer):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._timeslices = deque()
        
        ts = TimeSlice("title", 25, 's')
        ts.attachObserver(self)
        self._timeslices.append(ts)

        ts = TimeSlice("pause", 5, 's')
        ts.attachObserver(self)        
        self._timeslices.append(ts)

#        self._external_interruption = interruption()
#        self._internal_interruption = interruption()


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

    def update(self, subject, param):
        if(param):
            self._notify("TimeSlice", subject.get_title(), "'" +  param + "'")

    def _notify(self, title, subtitle, message):
        # dirty hack move implementation to ui layer
        # http://stackoverflow.com/questions/17651017/python-post-osx-notification
        t = '-title {!r}'.format(title)
        s = '-subtitle {!r}'.format(subtitle)
        m = '-message {!r}'.format(message)
        print(subtitle, message)
        os.system('/usr/local/bin/terminal-notifier {}'.format(' '.join([m, t, s])))
    
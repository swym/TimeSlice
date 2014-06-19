'''
Created on May 27, 2014

@author: alexandermertens
'''
from threading import Thread
from time import sleep
from util.observer.Subject import Subject
from datetime import timedelta, datetime


class Watchdog(Thread, Subject):
    '''
    classdocs
    '''


    def __init__(self, duration):
        '''
        Constructor
        '''
        Thread.__init__(self)
        Subject.__init__(self)
        
        self._duration   = timedelta(seconds = duration)
        self._startTime  = None
        
        self._running    = False
        self._alive      = True

        
    def run(self):
        while self._alive:
            
            self.reset()
            
            self._update()
            while self._running:
                sleep(0.5)
                self._update()
            
            if self._alive:    
                self.notifyObservers("fired")

    def _update(self):
        if (self._startTime + self._duration) <= self._my_now():
            self._running = False

    def _my_now(self):
        now = datetime.now()
        return timedelta(hours = now.hour, minutes = now.minute, seconds = now.second)
 

    def stop(self):
        self._alive = False
        self._running = False

        self.notifyObservers("stopped")
        
    def reset(self):
        self._startTime = self._my_now()
        self._running = True
        self.notifyObservers("resetted")

'''
Created on May 20, 2014

@author: alexandermertens
'''

from collections import deque

class Subject(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._observers = deque()

    
    def attach(self, observer):
        self._observers.append(observer)
        
    def detach(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, param = None):
        for obs in self._observers:
            obs.update(self, param)

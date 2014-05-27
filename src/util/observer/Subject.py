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

    
    def attachObserver(self, observer):
        self._observers.append(observer)
        
    def detachObserver(self, observer):
        self._observers.remove(observer)

    def notifyObservers(self, param = None):
        for obs in self._observers:
            obs.update(self, param)

'''
Created on Apr 9, 2014

@author: alexandermertens
'''

class Interruptions(object):
    '''
    classdocs
    '''


    def __init__(self, initial_interruptions = 0):
        '''
        Constructor
        '''
        self._interruptions = initial_interruptions
        
    def inc(self):
        self._interruptions += 1
        
    def get(self):
        return self._interruptions
        
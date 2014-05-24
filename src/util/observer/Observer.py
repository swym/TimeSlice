'''
Created on May 20, 2014

@author: alexandermertens
'''

class Observer(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    
    def update(self, subject, param):
        raise NotImplementedError
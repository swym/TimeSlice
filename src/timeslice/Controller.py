'''
Created on Apr 4, 2014

@author: swym
'''
from timeslice.Timer import Timer
from datetime import datetime

class Controller(object):
    '''
    classdocs
    '''


    def __init__(self, task, durationTask = 25, durationPause = 5):
        '''
        Constructor
        '''
        self.task = task
        self.timer = Timer(durationTask, durationPause)

        self.externalInterrupt = 0
        self.internalInterrupt = 0
        

        print(self.task, self.timer.duration, durationPause)
    
    def getCurrentTime(self):
        return datetime.now()
    
    def start(self):
        self.timer.start()
        
    def halt(self):
        self.timer.halt()
    
    def resume(self):
        self.timer.resume()
        
    def stop(self):
        self.timer.terminate()

    def incExternalInterrupt(self):
        self.externalInterrupt += 1
    
    def incInternalInterrupt(self):
        self.internalInterrupt += 1

    

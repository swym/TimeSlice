'''
Created on Apr 4, 2014

@author: swym
'''
from timeslice.TimerState import TimerState
from datetime import timedelta, datetime

class Timer(object):
    '''
    classdocs
    '''
    
    def __init__(self, duration, halt):
        '''
        Constructor
        '''
        self.duration  = timedelta(minutes = duration)
        self.maxHalt   = timedelta(minutes = halt)
        self.startTime = None
        self.haltTime  = None
        
        self.state = TimerState.inited

        
    def start(self):
        if self.state == TimerState.inited:
            self.startTime = datetime.now()
            self.state     = TimerState.running
 
    def halt(self):
        if self.state == TimerState.running:
            self.haltTime  = datetime.now()
            self.state     = TimerState.halted
        
    def resume(self):
        if self.state == TimerState.halted:
        # TODO: Pausenzeit einrichnen 
            self.state = TimerState.running
        
    def terminate(self):
        self.state = TimerState.terminated
   
    def update(self):
        # do some clever timer arithmetic and set state
        if self.state == TimerState.running:    
            if (self.startTime + self.duration) > datetime.now():
                self.state = TimerState.running
            else:
                self.state = TimerState.terminated
        
        return self.state
    
    def getRemainingTimer(self):
        if self.state == TimerState.inited:
            return self.duration
        if self.state == TimerState.halted:
            return self.haltTime + self.maxHalt - datetime.now()
        else:
            return self.startTime + self.duration - datetime.now()


    def isRunning(self):
        if self.update() == TimerState.running:
            return True
        else:
            return False
 
    def isHalted(self):
        if self.update() == TimerState.halted:
            return True
        else:
            return False

    def isTerminated(self):
        if self.update() == TimerState.terminated:
            return True
        else:
            return False
        
    def isInited(self):
        if self.update() == TimerState.inited:
            return True
        else:
            return False
        

        
                
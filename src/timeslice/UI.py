'''
Created on Apr 7, 2014

@author: swym
'''
import curses
from timeslice.Controller import Controller

class UI(object):
    '''
    classdocs
    '''


    def __init__(self, task, durationTask = 25, durationPause = 5):
        '''
        Constructor
        '''
        self.controller = Controller(task, durationTask, durationPause)
        self.screen = None 
        
        
        
        self.initScreen()
        self.startScreen()
        
    def __del__(self):
        curses.endwin()
        self.screen = None
        

        
    def initScreen(self):
        
        
        
        # create curses instance
        self.screen = curses.initscr()
        
        # input with getch() shall not block
        self.screen.nodelay(True)
        
        # init border
        self.screen.border(" ", " ", " ", " ", " ", " ", " ", " ")
    
    
    def startScreen(self):
        
    
        while not self.controller.timer.isTerminated():
        #while True:
            self.refreshScreen()
            self.readUserInput()
            curses.napms(250)
        curses.endwin()
        
    def refreshScreen(self):
        
        self.screen.clear()
        self.screen.refresh()
        
        remaining =  "remaining: " + str(self.controller.timer.getRemainingTimer())
        state = "state: " + str(self.controller.timer.state)
        now = str(self.controller.getCurrentTime())
        interrupts = "i: " + str(self.controller.internalInterrupt) + "   e: " + str(self.controller.externalInterrupt)      
    
          
        self.screen.addstr(0, 2, now)
        self.screen.addstr(2, 2, state)
        self.screen.addstr(3, 2, remaining)
        self.screen.addstr(4, 2, interrupts)
        
        if self.controller.timer.isRunning():
            self.screen.addstr(5, 4, "h - halt session")
        elif self.controller.timer.isHalted():
            self.screen.addstr(5, 4, "r - resume session")
        else:
            self.screen.addstr(5, 4, "s - start session")
          
        self.screen.addstr(6, 4, "i - internal interrupt")
        self.screen.addstr(7, 4, "e - external interrupt")
        
        self.screen.addstr(9, 4, "q - Exit")
        self.screen.addstr(10, 4, "")


    def readUserInput(self):
        
        c = self.screen.getch()   

        if c == ord("?"):
            #self.controller.incExternalInterrupt()
            pass
          
        if c == ord("s"):
            self.controller.start()
        if c == ord("r"):
            self.controller.resume()
        if c == ord("h"):
            self.controller.halt()
        if c == ord("q"):
            self.controller.stop()
        if c == ord("i"):
            self.controller.incInternalInterrupt()
        if c == ord("e"):
            self.controller.incExternalInterrupt()

    
        
        
        
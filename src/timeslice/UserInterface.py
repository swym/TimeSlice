'''
Created on Apr 10, 2014

@author: alexandermertens
'''
from timeslice.Session import Session
import curses

class UserInterface(object):
    '''
    classdocs
    '''


    def __init__(self, title, durationActive, durationPause):
        '''
        Constructor
        '''
        self._session = Session(title, durationActive, durationPause)
        self._screen = None
        
        self._init_screen()
        self._start_screen()


    def __del__(self):
        curses.endwin()
        self._screen = None
        
    def _init_screen(self):
        # create curses instance
        self._screen = curses.initscr()

        # input with getch() shall not block
        self._screen.nodelay(True)

    def _start_screen(self):

        while True:
            self._screen.clear()
            self._screen.refresh()

            # set border
            # self._screen.border()

            self._screen.addstr(2, 2, "Hello World!")
            
            c = self._screen.getch()
            if c == ord("q"):
                break
            
            curses.napms(100)
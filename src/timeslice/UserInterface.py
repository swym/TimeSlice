'''
Created on Apr 10, 2014

@author: alexandermertens
'''
from timeslice.Session import Session
import curses
from _curses import flash

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
        self._run_screen = True
        self._big_numbers_dict = None
        
        self._init_screen()
        self._init_big_numbers_dict()
        self._start_screen()


    def __del__(self):
        curses.endwin()
        self._screen = None
        
    def _init_screen(self):
        # create curses instance
        self._screen = curses.initscr()

        # input with getch() shall not block
        self._screen.nodelay(True)
        
    def _init_big_numbers_dict(self):
        
        self._big_numbers_dict = dict()

        big_number = []
        big_number.append("  ___  ")
        big_number.append(" / _ \ ")
        big_number.append("| | | |")
        big_number.append("| |_| |")
        big_number.append(" \___/ ")
        self._big_numbers_dict["0"] = big_number
    
        big_number = []
        big_number.append(" _ ")
        big_number.append("/ |")
        big_number.append("| |")
        big_number.append("| |")
        big_number.append("|_|")
        self._big_numbers_dict["1"] = big_number
    
        big_number = []
        big_number.append(" ____  ")
        big_number.append("|___ \ ")
        big_number.append("  __) |")
        big_number.append(" / __/ ")
        big_number.append("|_____|")
        self._big_numbers_dict["2"] = big_number
    
        big_number = []
        big_number.append(" _____ ")
        big_number.append("|___ / ")
        big_number.append("  |_ \ ")
        big_number.append(" ___) |")
        big_number.append("|____/ ")
        self._big_numbers_dict["3"] = big_number
    
        big_number = []
        big_number.append(" _  _   ")
        big_number.append("| || |  ")
        big_number.append("| || |_ ")
        big_number.append("|__   _|")
        big_number.append("   |_|  ")
        self._big_numbers_dict["4"] = big_number
    
        big_number = []
        big_number.append(" ____  ")
        big_number.append("| ___| ")
        big_number.append("|___ \ ")
        big_number.append(" ___) |")
        big_number.append("|____/ ")
        self._big_numbers_dict["5"] = big_number
    
        big_number = []
        big_number.append("  __   ")
        big_number.append(" / /_  ")
        big_number.append("| '_ \ ")
        big_number.append("| (_) |")
        big_number.append(" \___/ ")
        self._big_numbers_dict["6"] = big_number
          
        big_number = []
        big_number.append(" _____ ")
        big_number.append("|___  |")
        big_number.append("   / / ")
        big_number.append("  / /  ")
        big_number.append(" /_/   ")
        self._big_numbers_dict["7"] = big_number
    
        big_number = []
        big_number.append("  ___  ")
        big_number.append(" ( _ ) ")
        big_number.append(" / _ \ ")
        big_number.append("| (_) |")
        big_number.append(" \___/ ")
        self._big_numbers_dict["8"] = big_number
    
        big_number = []
        big_number.append("  ___  ")
        big_number.append(" / _ \ ")
        big_number.append("| (_) |")
        big_number.append(" \__, |")
        big_number.append("   /_/ ")
        self._big_numbers_dict["9"] = big_number
        
        big_number = []
        big_number.append("   ")
        big_number.append(" _ ")
        big_number.append("(_)")
        big_number.append(" _ ")
        big_number.append("(_)")
        self._big_numbers_dict[":"] = big_number

    def _start_screen(self):

        while self._run_screen:
            
            self._refresh_screen()
            self._get_user_input()           
            curses.napms(125)
            
    def _refresh_screen(self):
        self._screen.clear()
        self._screen.refresh()

        # set border
        # self._screen.border()
        if self._session.has_timeslices():
            ts_title = self._session.get_current_timeslice_title()

            ts_state = ""
            if self._session.is_current_timeslice_inited():
                ts_state = "inited"
            elif self._session.is_current_timeslice_running():
                ts_state = "running"
            elif self._session.is_current_timeslice_completed():
                ts_state = "completed"
            elif self._session.is_current_timeslice_cancelled():
                ts_state = "cancelled"

            # TODO: implement session-getter for remaining time
            ts_duration = str(self._session.get_current_timeslice().get_remaining_time())

            self._screen.addstr(1, 2, "Title: " + ts_title)
            self._screen.addstr(2, 2, "State: " + ts_state)
            self._screen.addstr(3, 2, "duration: " + ts_duration)
            self._add_big_numbers(4, 2, ts_duration.partition('.')[0])
            self._screen.addstr(10, 2, "Interruptions:")
            self._screen.addstr(11, 4, "internal: " + str(self._session.get_current_timeslice_internal_interruptions()))
            self._screen.addstr(12, 4, "external: " + str(self._session.get_current_timeslice_external_interruptions()))


            # options
            if self._session.is_current_timeslice_inited():
                self._screen.addstr(13, 4, "s - start")
            elif self._session.is_current_timeslice_running():
                self._screen.addstr(13, 4, "i - internal interruption")
                self._screen.addstr(14, 4, "e - external interruption")
                self._screen.addstr(15, 4, "c - cancel")
            elif (self._session.is_current_timeslice_completed() or
                  self._session.is_current_timeslice_cancelled()):
                self._screen.addstr(13, 4, "n - next")

            self._screen.addstr(18, 4, "q - quit session")
            self._screen.addstr(19, 4,"") # Cursor for user input
        else:
            self._screen.addstr(2, 4, "session queue empty - good job! :-)")
            self._screen.addstr(5, 4, "q - quit session")
    
    def _get_user_input(self):
        c = self._screen.getch()
        if c == ord("c"):
            self._session.cancel_current_timeslice()
        elif c == ord("s"):
            self._session.start_current_timeslice()
        elif c == ord("i"):
            self._session.inc_current_timeslice_internal_interruptions()
        elif c == ord("e"):
            self._session.inc_current_timeslice_external_interruptions()
        elif c == ord("n"):
            self._session.next_timeslice()
        elif c == ord("q"):
            self._run_screen = False
            
    def _add_big_numbers(self, row, col, number_string):
        
        # iterate over every char in string
        for char in number_string:
            #look up char in dictonary
            if char in self._big_numbers_dict:
                #if found
                for i in range(0, len(self._big_numbers_dict[char])):
                    #add number row by row to screen
                    self._screen.addstr(row + i, col, self._big_numbers_dict[char][i])
                # move col-pointer directly behind last printed number
                col = col + len(self._big_numbers_dict[char][0])

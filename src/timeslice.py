'''
Created on Apr 4, 2014

@author: swym
'''
#from timeslice.Controller import Controller
from datetime import datetime, time, timedelta
from time import sleep
from timeslice.Session import Session
from timeslice.UserInterface import UserInterface


def develop_session():
    #ui = UI("new task!")
    #crtl = Controller("task")
    s = Session("aSession")
    print(s.get_timeslice_count())
    i = 0
    while s.has_timeslices():
        i += 1
        print(str(i) + ": before start: ", s.get_current_timeslice())
        s.start_current_timeslice()
        print(str(i) + ": before sleep: ", s.get_current_timeslice())
        if i == 1:
            s.inc_current_timeslice_external_interruptions()
            s.inc_current_timeslice_external_interruptions()
            s.inc_current_timeslice_external_interruptions()
            s.inc_current_timeslice_external_interruptions()
        else:
            s.inc_current_timeslice_internal_interruptions()
            s.inc_current_timeslice_internal_interruptions()

        print("ext:", s.get_current_timeslice_external_interruptions())
        print("int:", s.get_current_timeslice_internal_interruptions())
        
        sleep(5)
        s.is_current_timeslice_running()
        print(str(i) + ": after sleep : ", s.get_current_timeslice())

        print(str(i) + ": try cancel  : ",s.cancel_current_timeslice())
        print(str(i) + ": after cancel: ", s.get_current_timeslice())
        
        s.next_timeslice()
        print("> next >", s.get_timeslice_count())
    print("+++ end +++")
    
#     s.start()
#     print(s.getCurrentTimeSliceTitle(), s.getCurrentTimeSliceDuration())
#     sleep(7)
#     print("completed?", s.isCurrentTimeSliceCompleted())
#     print("canceled?", s.cancel())
#     s.next()
#     s.start()
#     print(s.getCurrentTimeSliceTitle(), s.getCurrentTimeSliceDuration())
#     print("completed?", s.isCurrentTimeSliceCompleted())
#     print("canceled?", s.cancel())
#     s.next()
#     s.start()
#     print(s.getCurrentTimeSliceTitle(), s.getCurrentTimeSliceDuration())
#     print("completed?", s.isCurrentTimeSliceCompleted())
#     print("canceled?", s.cancel())
#     s.next()
#     s.start()
    

def develop_ui():
    
    ui = UserInterface("new userinterface", 25, 5)
    
    pass

if __name__ == '__main__':
    
    develop_ui()
    

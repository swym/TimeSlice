'''
Created on Apr 4, 2014

@author: swym
'''
#from timeslice.Controller import Controller
from timeslice.UI import UI
from timeslice.Timer import Timer
from datetime import datetime, time, timedelta
from time import sleep


def develop_timer():
    
    aTimer = Timer(1, 5)
    
    print(aTimer.state)
    print(aTimer.duration.seconds)
    print(datetime.now(), datetime.now() + aTimer.duration)
    
    aTimer.start()
    
    while not aTimer.isTerminated():
        # aTimer.update()
        # print(datetime.now(), aTimer.startTime)
        
        res = aTimer.getRemainingTimer()
        
        # print(res)
        # print nice formated rest time of Timer
        str_res = str(res).partition('.')[0]
        nice_res = str_res.split(sep=':')[1] + ":" + str_res.split(sep=':')[2]  
        print(nice_res)

        sleep(1)
        
    print("end")


if __name__ == '__main__':
    
    ui = UI("new task!")
    #crtl = Controller("task")
    

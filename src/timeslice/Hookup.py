'''
Created on May 27, 2014

@author: alexandermertens
'''
from os.path import os
import logging

class Hookup(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        homedir = os.path.expanduser("~")
        logging.basicConfig(filename=homedir + '/.timeslice/timeslice.log',
                            level=logging.DEBUG,
                            format='%(asctime)s | %(levelname)s | %(message)s')
    
    def hookup_start(self, timeslice):
        self._osx_notification('TimeSilce.py',
                               "'" + str(timeslice.get_duration()) + "'",
                               'Be productive! :)')
        
        logmsg = "START | timeslice '" + timeslice.get_title() + \
                 "' (" + str(timeslice.get_duration()) + ")"
        logging.info(logmsg)

    def hookup_complete(self, timeslice):
        self._osx_notification('TimeSilce.py',
                               "'" + timeslice.get_title() + "'",
                               'Yay you made it! :D')
        
        logmsg = "COMPLETED | timeslice '" + timeslice.get_title() + \
                 "' (" + str(timeslice.get_duration()) + ") ints: (ext: " + \
                 str(timeslice.get_external_interruptions()) + " int: " + \
                 str(timeslice.get_internal_interruptions()) + ")"
        logging.info(logmsg)
        
    def hookup_cancelled(self, timeslice):
        self._osx_notification('TimeSilce.py',
                               "'" + timeslice.get_title() + "'",
                               'Aww! :( Next time you have more luck.')
        
        logmsg = "CANCELLED | timeslice '" + timeslice.get_title() + \
                 "' (" + str(timeslice.get_duration()) + ") ints: (ext: " + \
                 str(timeslice.get_external_interruptions()) + " int: " + \
                 str(timeslice.get_internal_interruptions()) + ") " + \
                 "time left: " + str(timeslice.get_remaining_time())
        logging.info(logmsg)
        
    def hookup_interrupted(self, timeslice):
        logmsg = "INTERRUPT | timeslice '" + timeslice.get_title() + \
                 "' (" + str(timeslice.get_duration()) + ") ints: (ext: " + \
                 str(timeslice.get_external_interruptions()) + " int: " + \
                 str(timeslice.get_internal_interruptions()) + ") " + \
                 "time left: " + str(timeslice.get_remaining_time())
        logging.debug(logmsg)

    def hookup_watchdog_fired(self):
        self._osx_notification('TimeSilce.py', '',
                               'Watchdog fired! - come back to me! ;-)')

    def _osx_notification(self, title, subtitle, message):
        # http://stackoverflow.com/questions/17651017/python-post-osx-notification
        t = '-title {!r}'.format(title)
        s = '-subtitle {!r}'.format(subtitle)
        m = '-message {!r}'.format(message)
        os.system('/usr/local/bin/terminal-notifier {}'.format(' '.join([m, t, s])))
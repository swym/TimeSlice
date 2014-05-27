'''
Created on May 27, 2014

@author: alexandermertens
'''
from os.path import os

class Hookup(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def hookup_start(self, message):
        self._osx_notification('TimeSilce.py', "'" + message + "'", 'Be productive! :)')

    def hookup_complete(self, message):
        self._osx_notification('TimeSilce.py', "'" + message + "'", 'Yay you made it! :D')
        
    def hookup_cancelled(self, message):
        self._osx_notification('TimeSilce.py', "'" + message + "'", 'Aww! :( Next time you have more luck.')

    
    def _osx_notification(self, title, subtitle, message):
        # http://stackoverflow.com/questions/17651017/python-post-osx-notification
        t = '-title {!r}'.format(title)
        s = '-subtitle {!r}'.format(subtitle)
        m = '-message {!r}'.format(message)
        os.system('/usr/local/bin/terminal-notifier {}'.format(' '.join([m, t, s])))
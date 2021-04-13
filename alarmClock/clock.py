import os

class Clock(object):
    '''Initialized with the New Alarm window, a new `Clock` is created after closing the window
    Allows for user customizable time and days the alarm will go off.
    The alarm can be further customized in the Edit Alarm window'''
    def __init__(self, hour, minute, period, days):
        self._hour = hour
        self._minute = minute
        self._period = period
        self._days = days
        self._name = 'Alarm'
        self._on = True
        self._soundDir = 'data/sounds'
        self._sound = 'siren.ogg'

    def __str__(self):
        '''Returns a formatted str, ex: `04:01 PM`'''
        return f'{self._hour}:{self._minute} {self._period}'

    @property
    def time(self):
        return (self._hour, self._minute, self._period)

    @time.setter
    def time(self, newTime):
        self._hour, self._minute, self._period = newTime

    @property
    def days(self):
        return self._days

    @days.setter
    def days(self, value):
        self._days = value if value == [] else value
 
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = 'Alarm' if value == '' else value

    @property
    def on(self):
        return self._on
    
    @on.setter
    def on(self, value):
        self._on = value

    @property
    def soundDir(self):
        return self._soundDir

    @soundDir.setter
    def soundDir(self, value):

        self._soundDir = value

    @property
    def sound(self):
        return self._sound 

    @sound.setter
    def sound(self, value):
        self._sound = 'siren.ogg' if not self.fileExists(self.soundDir, value) else value

    def fileExists(self, directory, fileName):
        '''Determines if a file path exists, returns bool value
        -> directory (str): the file path to a directory, /formatted/like/this
        -> fileName (str): a file in the directory'''

        return os.path.exists(os.path.join(directory, fileName))
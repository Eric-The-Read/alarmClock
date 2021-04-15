import os
import pickle
from datetime import datetime

import PySimpleGUI as sg

from alarmClock.clock import Clock
from alarmClock.settings import clocks, dateFmt
from alarmClock.windows import alarmPlaying, dateOptions, editAlarm, newAlarm

def main():
    layout = [
                [
                    sg.Text(text=datetime.now().strftime(dateFmt[0]), auto_size_text=True, key='-Date-'), 

                    sg.Button('Date Options', key='-DateOptions-'),
                ],
                [
                    sg.Button('+ New Alarm', size=(33, 1), key='-NewAlarm-'), 
                ],
                [
                    sg.HSeparator(),

                ],
                [
                    sg.Listbox(values=[str(i) for i in clocks], enable_events=True, size=(35, 5), key='-AlarmList-'),
                ],
                [
                    sg.Button('Edit Alarm', key='-EditAlarm-'),
                    sg.Button('Delete Alarm', key='-DeleteAlarm-'),
                    sg.Exit(),
                ]
            ]

    window = sg.Window('Alarm Clock', layout)
    opened = True                            

    while True:
        event, values = window.read(timeout=1000)               #Reads events every second

        if opened == True:                                      #When window is opened load instances of 
            with open(f'data/clock.pickle', 'rb') as inF:       #`Clock` class from data/clock.pickle
                while True:
                    try:
                        clocks.append(pickle.load(inF))         #Append the data to `clocks` list in settings.py
                    except EOFError:                            #while there are still items in clock.pickle
                        break

            window['-AlarmList-'].update([str(i) for i in clocks])  #Populate `-AlarmList-` w/ str representations
                                                                    #of each instance of the Clock class from the `clocks` list
            opened = False                                          #Set opened to False so clocks.pickle is only accessed once 
                                                                        
        elif event in ['Exit', sg.WIN_CLOSED]:                      
            with open(f'data/clock.pickle', 'wb') as outF:          #When main window is closed, overwrite clock.pickle
                                                                    #w/ the items in the `clocks` list
                for clock in clocks:
                    pickle.dump(clock, outF, -1)
            opened = False
            break

        elif event == '-DateOptions-':                          #If the 'Date Options' button is clicked
            dateOptions.dateOptions()                           #the dateOptions window is opened.

        elif event == '-NewAlarm-':                                 #If the 'New Alarm' button is clicked
            newAlarm.newAlarm()                                     #the newAlarm window is opened.
            window['-AlarmList-'].update([str(i) for i in clocks])  #then `-AlarmList-` is updated with the new alarm

        elif event == '-EditAlarm-' and len(values['-AlarmList-']): #If an alarm is selected when the 'Edit Alarm' 
                                                                    #button is clicked
            for clock in clocks:                                    #iterate over the `clocks` list until  
                if str(clock) == values['-AlarmList-'][0]:          #correct clock is found. 
                    editAlarm.editAlarm(clock)                      #Open 'Edit Alarm' window with selected clock instance
                    window['-AlarmList-'].update([str(i) for i in clocks])  #update '-AlarmList-' after 'Edit Alarm' is closed
                                                                    
        elif event == '-DeleteAlarm-' and len(values['-AlarmList-']):   #If an alarm is selected and the 'Delete Alarm'
            sg.popup("Alarm Deleted")                                   #button is clicked, delete the alarm
            for clock in clocks:
                if str(clock) == values['-AlarmList-'][0]:               
                    clocks.remove(clock)                                #Then remove the alarm from the `clocks` list
                    window['-AlarmList-'].update([str(i) for i in clocks]) #and update '-AlarmList-'

        for clock in clocks:
            if (str(clock) == datetime.now().strftime('%I:%M %p') and   #Basically, if the current time matches any clock
            clock.on and datetime.today().weekday() in clock.days):     #and that clock is on and the alarm is set to play
                                                                        #on the current day of the week
                alarmPlaying.alarmPlaying(clock)                        #open the 'Alarm Playing' window.
            else:
                continue                                                

        window['-Date-'].update(datetime.now().strftime(dateFmt[0]))    #updates the time text box with the date format specified
                                                                        #in `dateFmt` list in settings.py
    window.close()  

if __name__ == '__main__':
    main()

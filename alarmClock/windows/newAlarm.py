import PySimpleGUI as sg
from alarmClock.clock import Clock
from alarmClock.settings import dayList, hourList, minuteList, periodList, clocks

def newAlarm():
    '''Opens window to create a new alarm, and select days in which alarm plays.'''

    layout = [
        [
            sg.Combo(hourList, size=(3, 1), key="-Hour-", default_value='12'),
            sg.Text(":"),
            sg.Combo(minuteList, size=(3, 1), enable_events=True, key="-Minute-", default_value='01'),
            sg.Combo(periodList, size=(3, 2), enable_events=True, key='-Period-', default_value='PM'),
        ],
        [
            sg.Listbox(dayList, key='-DaySelect-', size=(25, 8), select_mode='multiple'),
        ],
        [
            sg.Submit(),
            sg.Exit(),
        ],
    ]

    window = sg.Window("New Alarm", layout, finalize=True)

    for i in [window['-Hour-'], window['-Minute-'],window['-Period-']]: #Bind window elements in list to <Enter> 
        i.bind('<Enter>', 'Enter-')                                     #creating `i=Enter-` event, causing the associated
                                                                        #combo box to drop down automatically on mouse over
    while True:
        event, values = window.read()
    
        if event in ['Exit', sg.WIN_CLOSED]:
            break
        
        elif event == '-Hour-Enter-':
            window['-Hour-'].Widget.event_generate('<Button-1>')
        
        elif event == '-Minute-Enter-':
            window['-Minute-'].Widget.event_generate('<Button-1>')

        elif event == '-Period-Enter-':
            window['-Period-'].Widget.event_generate('<Button-1>')

        elif event == 'Submit':                                            
            daysOn = [idx for idx, i in enumerate(dayList) if i in values['-DaySelect-']] #Maps days selected in `-DaySelect-` to ints

            clocks.append(Clock(values['-Hour-'], values['-Minute-'], values['-Period-'], daysOn)) #create a new 
                                                                                            #instance of the `Clock` class
            break

    window.close()
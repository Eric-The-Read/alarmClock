import os
import PySimpleGUI as sg
from pygame import mixer
from alarmClock.clock import Clock
from alarmClock.settings import dayList, hourList, minuteList, periodList

def editAlarm(clockInstance):
    '''Opens window to edit and customize the selected alarm clock, which is an instance of the `Clock` class. 
    When closed, updates selected `Clock` instance with the selected properties.
    ->clockInstance = instance of `Clock` class, found in `clocks` in settings.
    '''

    mixer.init()

    layout = [
        [
            sg.Combo(hourList, size=(3, 1), key="-EditHour-", default_value=clockInstance.time[0]),
            sg.Text(":"),
            sg.Combo(minuteList, size=(3, 1), enable_events=True, key="-EditMinute-", default_value=clockInstance.time[1]),
            sg.Combo(periodList, size=(3, 2), enable_events=True, key='-EditPeriod-', default_value=clockInstance.time[2]),
            sg.Button('On', size=(3, 1), button_color=('green'), key='-EditStatus-'),
        ],
        [
            sg.Text('Name: '),
            sg.Input(key='-EditName-', size=(35,1), default_text=clockInstance.name),
        ],
        [   
            sg.Text('Select Folder:'),
            sg.In(size=(30, 1), enable_events=True, key='-EditSoundFolder-', default_text=clockInstance.soundDir),
            sg.FolderBrowse(),
        ],
        [
            sg.Listbox(values=[f for f in os.listdir(clockInstance.soundDir) if os.path.isfile(             #values creates a list of files in the `Clock` instance
                os.path.join(clockInstance.soundDir, f)) and f.lower().endswith(('.mp3', '.wav', '.ogg'))      #soundDir that end with .mp3, .wav or .ogg
            ], enable_events=True, size=(30, 20), key='-FileList-', default_values=clockInstance.sound), 
            sg.Listbox(values=dayList, size=(20,20), key='-EditDays-', select_mode='multiple', default_values=[dayList[i] for i in clockInstance.days]),
        ],
        [
            sg.Button('Preview', size=(7, 0), key='-Preview-'),
            sg.Submit(),
            sg.Exit(),
        ],
    ]

    window = sg.Window('Edit Alarm', layout, finalize=True)

    preview = False
    fileName = False

    status = True

    for i in [window['-EditHour-'], window['-EditMinute-'], window['-EditPeriod-']]: #Binds window elements in list to <Enter>
        i.bind('<Enter>', 'Enter-')                                                  #creating `i-Enter` event, causing the associated
                                                                                     #combo box to drop down automatically on mouse over
    while True:
        event, values = window.read()

        if event in ['Exit', sg.WIN_CLOSED]:
            mixer.music.stop()
            mixer.music.unload()
            break
        
        elif event == '-EditHour-Enter-':
            window['-EditHour-'].Widget.event_generate('<Button-1>')
        
        elif event == '-EditMinute-Enter-':
            window['-EditMinute-'].Widget.event_generate('<Button-1>')

        elif event == '-EditPeriod-Enter-':
            window['-EditPeriod-'].Widget.event_generate('<Button-1>')

        elif event == '-EditSoundFolder-':                         #When 'Browse' button is clicked
            folder = values['-EditSoundFolder-']                               
            try:
                fileList = os.listdir(folder)                      #The current files in the folder are accessed
            except:
                fileList = []

            fnames = [f for f in fileList if os.path.isfile(        #and `-FileList-` is updated if any of the files
                os.path.join(folder, f)) and f.lower().endswith(('.mp3', '.wav', '.ogg')) #end with.mp3, .wav or .ogg
            ]
            window['-FileList-'].update(fnames)
        
        elif event == '-FileList-':                                 #If an item in the `-FileList-` is clicked
            try:                                                    #it is either saved to the `fileName` variable
                fileName = os.path.join(values['-EditSoundFolder-'], values['-FileList-'][0]) 
            except Exception:
                sg.popup('No file selected')                        #or a popup occurs when no file is selected
                break                       

        elif event == '-EditStatus-':                               #Toggles alarm on/off, uses status flag to update 
            status = not status                                     #button with the current selection
                                                                    #when clicked, alarm is turned off. When clicked again
                                                                    #the alarm turns back on
            window['-EditStatus-'].Update(('Off', 'On')[status], button_color=('white', ('red', 'green')[status]))

        elif event == '-Preview-':                                      #Works the same as the on/off button, but to start and
            window['-Preview-'].Update(('Stop', 'Preview')[preview])    #a preview of the selected alarm sound.
            preview = not preview   

            if preview == True and not fileName:                        #if no file is selected, the current default 
                mixer.music.load(f'{clockInstance.soundDir}/{clockInstance.sound}') #alarm tone for the alarm is played
                mixer.music.play(loops=-1)

            elif preview == True and fileName:                         #Otherwise the selected sound is played
                mixer.music.load(fileName)
                mixer.music.play(loops=-1)

            elif preview == False:                                     #when the stop button is clicked, the music stops
                mixer.music.stop()
                mixer.music.unload()

        elif event == 'Submit':                                         #Updates the `Clock` instance with the changes made
            mixer.music.stop()
            daysOn = [idx for idx, i in enumerate(dayList) if i in values['-EditDays-']]
            clockInstance.time = (values['-EditHour-'], values['-EditMinute-'], values['-EditPeriod-']) #updates the time the alarm will play
            clockInstance.days = daysOn                                 #updates the days the alarm will play
            clockInstance.name = values['-EditName-']                   #updates `name`
            clockInstance.soundDir = values['-EditSoundFolder-']        #updates sound directory
            clockInstance.sound = values['-FileList-'][0]               #updates the sound that will play when the alarm goes off
            clockInstance.on = status                                   #updates the status of the alarm (on/off)
            break

    window.close()
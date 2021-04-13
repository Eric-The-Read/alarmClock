from pygame import mixer
import PySimpleGUI as sg

def alarmPlaying(clockInstance):
    '''Opens window when alarm is playing. Stops playing sound when window is closed.
    -> clockInstance = instance of `Clock` class, found in `clocks` in settings
    '''
    
    mixer.init()

    layout = [
        [
            sg.Text(clockInstance.name),
        ],
        [
            sg.OK(),
        ]
    ]
    window = sg.Window('Alarm', layout)
    while True:
        mixer.music.load(f'{clockInstance.soundDir}/{clockInstance.sound}') #When window opens, it loads and plays 
        mixer.music.play(loops=-1)                                          #The alarm selected in the 'Edit Alarm' window.
        
        event, values = window.read()

        if event in ['OK', sg.WINDOW_CLOSED]:                               #Alarm stops playing after window is closed.
            mixer.music.stop()
            mixer.music.unload()
            clockInstance.on = False
            break

    window.close()

import PySimpleGUI as sg
from alarmClock.settings import dateFmt

def dateOptions():
    '''Opens window to customize the format of the clock, based on the datetime module format codes.'''

    layout = [
        [
            sg.Text('Please specify a date and time format\nhttps://docs.python.org/3/library/datetime.html')
        ],
        [
            sg.InputText(key='-DateFormat-')
        ],
        [
            sg.Submit(),
            sg.Button('Default', enable_events=True, key='-DefaultFormat-'),
            sg.Exit(),
        ]
    ]
    window = sg.Window('Date & Time Format', layout, resizable=True, finalize=True)

    while True:

        event, values = window.read()
        
        if event in ['Exit', sg.WIN_CLOSED]:
            break

        elif event == '-DefaultFormat-':
            dateFmt[0] = "%m/%d/%Y %I:%M:%S %p"
            break

        elif event == 'Submit' and len(values['-DateFormat-']):
            dateFmt[0] = values['-DateFormat-']
            break
    
    window.close()

# * Pattern 2A - Persistent window (multiple reads using an event loop)
# The Persistent window is one that sticks around. 
# With these programs, you loop, reading and processing "events" such as button clicks. 
# It's more like a typical Windows/Mac/Linux program.

import PySimpleGUI as sg      

sg.theme('DarkAmber')    # Keep things interesting for your users

layout = [[sg.Text('Persistent window')],      
            [sg.Input(key='-IN-')],      
            [sg.Button('Read'), sg.Exit()]]      

window = sg.Window('Window that stays open', layout)      

while True:                             # The Event Loop
    event, values = window.read() 
    print(event, values)       
    if event == sg.WIN_CLOSED or event == 'Exit':
        break      

window.close()



# * Pattern 1A - "One-shot Window" - (The Simplest Pattern)
# The One-shot window is one that pops up, collects some data, and then disappears.
# It is more or less a 'form' meant to quickly grab some information and then be closed.

import PySimpleGUI as sg      

layout = [[sg.Text('My one-shot window.')],      
            [sg.InputText(key='-IN-')],      
            [sg.Submit(), sg.Cancel()]]      

window = sg.Window('Window Title', layout)    

event, values = window.read()    
window.close()

text_input = values['-IN-']    
sg.popup('You entered', text_input)
import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Cuál es tu nombre?')],
            [sg.Input(key='-INPUT-')],
            [sg.Text(size=(40,1), key='-OUTPUT-')],
            [sg.Button('Ok'), sg.Button('Salir')] ]

# Create the Window
window = sg.Window('Ventana de Identificación', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Salir': # if user closes window or clicks cancel
        break
    window['-OUTPUT-'].update('Hola ' + values['-INPUT-'] + '! Gracias por usar este programa')

window.close()
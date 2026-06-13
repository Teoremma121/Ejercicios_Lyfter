# Error Popups
# The editor and explorer are used by the Demo Browser as well as the PySimpleGUI Error with Traceback Popup window.
# This popup is used internally within PySimpleGUI and you can also use the same popup. 
# To use this popup, call popup_error_with_traceback like in this example:

import PySimpleGUI as sg

try:
    a = 1/0
except Exception as e:
    sg.popup_error_with_traceback('Error in the event loop', e, emoji=sg.EMOJI_BASE64_SCREAM)

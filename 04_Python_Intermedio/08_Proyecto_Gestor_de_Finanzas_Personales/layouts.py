import PySimpleGUI as sg
from datetime import datetime

def permanent_manager_window(manager):
    start = datetime.now().strftime("%d/%m/%Y")
    end = start
    headers = ["Fecha","Tipo","Categoría","Título","Monto"]    
    sg.theme('Light Blue 1')
    frame_layout1 = [[sg.Text('Fecha inicio:'),sg.Input(size=10,enable_events=True,default_text=start,key='-START-'),sg.CalendarButton('Calendario', target='-START-',format="%d/%m/%Y"),sg.Text('Fecha final:'), sg.Input(size=10,enable_events=True,default_text=end,key='-END-'),sg.CalendarButton('Calendario', target='-END-',format="%d/%m/%Y")],
                    [sg.Table(values=[], headings=headers, expand_x=True,justification="left",auto_size_columns=True,key='-TABLE-',text_color="#400000")],
                    [checkbox('Ingresos:','-CHECK-INCOMES-'), multiline(0,'-TOT-INCOMES-') , checkbox('Gastos:','-CHECK-EXPENSES-'), multiline(0,'-TOT-EXPENSES-'), sg.Text('Balance:'), multiline(0,'-BALANCE-')]]

    frame_layout2 = [[[sg.Checkbox(cat.name, default=True, key=f'-CAT-{cat.name.upper()}-', checkbox_color=cat.color, enable_events=True)] for cat in manager.categories]]

    frame_layout3 = [[sg.Button('Agregar ingreso', key='-INCOME-'),sg.Button('Agregar gasto', key='-EXPENSE-'),sg.Button('Crear Categoría', key='-CATEGORY-')]]

    layout = [[sg.Frame('Movimientos', frame_layout1), sg.Frame('Categorías', frame_layout2, vertical_alignment='t', expand_y=True, key='-CATS-')],
                [sg.Frame('Gestionar', frame_layout3, expand_x=True)]]

    window = sg.Window('Gestor de Finanzas Personales', layout, finalize=True)
    return window 

def checkbox(tag,key):
    element = sg.Checkbox(tag, default=True, key=key, enable_events=True)
    return element

def multiline(value,key):
    element = sg.Multiline(value,s=8,no_scrollbar=True,key=key)
    return element

def one_shot_movement_window(manager,type):
    date = datetime.now().strftime("%d/%m/%Y")
    translator = {'-INCOME-':'Ingreso','-EXPENSE-':'Gasto'}
    layout = [[sg.Text('Tipo', size=(8)), sg.Multiline(translator[type],s=8,no_scrollbar=True,key='-TYPE-',disabled=True)],
                [sg.Text('Fecha', size=(8)), sg.Input(size=12,default_text=date,key='-DATE-'), sg.CalendarButton('Calendario', target='-DATE-',format="%d/%m/%Y")],
                [sg.Text('Categoría', size=(8)), sg.Combo(values=[[cat.name][0] for cat in manager.categories],key='-CATEGORY-')],
                [sg.Text('Título', size=(8)), sg.InputText(key='-TITLE-')],
                [sg.Text('Monto', size=(8)), sg.Input(key='-AMOUNT-')],
                [sg.Button('Agregar'), sg.Button('Cancelar')]]
    window = sg.Window(f'Agregar {translator[type]}', layout)
    return window

def one_shot_create_category_window():
    layout = [[sg.Text('Categoría', size=(8)), sg.InputText(key='-NAME-')],
                [sg.ColorChooserButton('Elegir un color', target='-COLOR-'),sg.Text("",size=(2),background_color='white',key='-SAMPLE-'),sg.Input(enable_events=True, size=5, visible=False, key='-COLOR-')],
                [sg.Button('Crear'), sg.Button('Cancelar')]]
    window = sg.Window(f'Crear Categoría', layout)
    return window
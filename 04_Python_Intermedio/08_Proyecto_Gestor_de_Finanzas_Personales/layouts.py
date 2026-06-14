import PySimpleGUI as sg

def permanent_manager_window(manager):
    headers = ["Tipo","Categoría","Título","Monto"]    
    sg.theme('Light Blue 1')
    frame_layout1 = [[sg.Text('Fecha inicio:'), sg.Input(size=10, key='-START-'),sg.Text('Fecha final:'), sg.Input(size=10,key='-END-')],
                    [sg.Table(values=update_movements(manager), headings=headers, expand_x=True,justification="left",auto_size_columns=True,key='-TABLE-')],
                    [checkbox('Ingresos:'), multiline('-TOT_INCOMES-') , checkbox('Gastos:'), multiline('-TOT_EXPENSES-'), sg.Text('Balance:'), multiline('-BALANCE-')]]

    frame_layout2 = [[[sg.Checkbox(cat.name, default=True, key=f'-{cat.name.upper()}-', checkbox_color=cat.color)] for cat in manager.categories]]

    frame_layout3 = [[sg.Button('Agregar ingreso', key='-INCOME-'),sg.Button('Agregar gasto', key='-EXPENSE-'),sg.Button('Crear Categoría', key='-CATEGORY-')]]

    layout = [[sg.Frame('Movimientos', frame_layout1), sg.Frame('Categorías', frame_layout2, vertical_alignment='t', expand_y=True, key='-CATS-')],
                [sg.Frame('Gestionar', frame_layout3, expand_x=True)]]

    window = sg.Window('Gestor de Finanzas Personales', layout)
    return window 

def checkbox(tag):
    element = sg.Checkbox(tag, default=True)
    return element

def multiline(key):
    element = sg.Multiline(s=8,no_scrollbar=True,key=key)
    return element

def update_movements(manager):
    rows = [[move.type, move.category, move.title, move.amount] for move in manager.movements]
    return rows

def one_shot_movement_window(manager,type):
    translator = {'-INCOME-':'Ingreso','-EXPENSE-':'Gasto'}
    layout = [[sg.Text('Tipo', size=(8)), sg.Multiline(translator[type],s=8,no_scrollbar=True,key='-TYPE-',disabled=True)],
                [sg.Text('Categoría', size=(8)), sg.Combo(values=[[cat.name][0] for cat in manager.categories],key='-CATEGORY-')],
                [sg.Text('Título', size=(8)), sg.InputText(key='-TITLE-')],
                [sg.Text('Monto', size=(8)), sg.Input(key='-AMOUNT-')],
                [sg.Button('Agregar'), sg.Button('Cancelar')]]
    window = sg.Window(f'Agregar {translator[type]}', layout)
    return window

def one_shot_create_category_window():
    layout = [[sg.Text('Categoría', size=(8)), sg.InputText(key='-NAME-')],
                [sg.ColorChooserButton('Elegir un color', target='-COLOR-'),sg.Text("",size=(2),background_color='white',key='-SAMPLE-'),sg.Input(enable_events=True, size=5, visible=True, key='-COLOR-')],
                [sg.Button('Crear'), sg.Button('Cancelar')]]
    window = sg.Window(f'Crear Categoría', layout)
    return window
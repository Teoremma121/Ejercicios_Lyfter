import PySimpleGUI as sg
import func as f

def main():
    fm = f.Finance_Manager()
    interface_main_logic(fm)

def interface_main_logic(manager):
    window_1 = permanent_manager_window(manager)
    while True:
        event, values = window_1.read()
        if event != sg.WIN_CLOSED:
            if event in ('-INCOME-','-EXPENSE-'):
                window_2 = one_shot_movement_window(manager,event)
                event, values = window_2.read()
                if (event == 'Agregar') and (len(values) == 4):
                    manager.add_movement(values['-TYPE-'],values['-CATEGORY-'][0],values['-TITLE-'],values['-AMOUNT-'])
                window_2.close()
            window_1['-TABLE-'].update(values=update_movements(manager))
            if event == '-CATEGORY-':
                window_2 = one_shot_create_category_window()
                event, values = window_2.read()
                window_2.close()
        else:
            window_1.close()
            break

def permanent_manager_window(manager):
    
    sg.theme('Light Blue 1')

    frame_layout1 = [[sg.Text('Fecha inicio:'), sg.Input(size=10, key='-START-'),sg.Text('Fecha final:'), sg.Input(size=10,key='-END-')],
                    [sg.Table(values=update_movements(manager), headings=["Tipo","Categoría","Título","Monto"], expand_x=True,justification="left",auto_size_columns=True,key='-TABLE-')],
                    [checkbox('Ingresos:'), multiline('-TOT_INCOMES-') , checkbox('Gastos:'), multiline('-TOT_EXPENSES-'), sg.Text('Balance:'), multiline('-BALANCE-')]]

    frame_layout2 = [[[sg.Checkbox(cat.name, default=True, key=f'-{cat.name.upper()}-', checkbox_color=cat.color)] for cat in manager.categories],
                    [sg.Button('Crear Categoría', key='-CATEGORY-')]]

    frame_layout3 = [[sg.Button('Agregar ingreso', key='-INCOME-'),sg.Button('Agregar gasto', key='-EXPENSE-')]]

    layout = [[sg.Frame('Movimientos', frame_layout1), sg.Frame('Categorías', frame_layout2, vertical_alignment='t', expand_y=True)],
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
    layout = [[sg.Text('Tipo', size=(8)), sg.Multiline(translator[type],s=8,no_scrollbar=True,key='-TYPE-')],
                [sg.Text('Categoría', size=(8)), sg.Combo(values=[[cat.name] for cat in manager.categories],key='-CATEGORY-')],
                [sg.Text('Título', size=(8)), sg.InputText(key='-TITLE-')],
                [sg.Text('Monto', size=(8)), sg.Input(key='-AMOUNT-')],
                [sg.Button('Agregar'), sg.Button('Cancelar')]]
    window = sg.Window(f'Agregar {translator[type]}', layout)
    return window

def one_shot_create_category_window():
    layout = [[sg.Text('Categoría', size=(8)), sg.InputText(key='-CATEGORY-')],
                [sg.Button('Crear'), sg.Button('Cancelar')]]
    window = sg.Window(f'Crear Categoría', layout)
    return window

main()
    







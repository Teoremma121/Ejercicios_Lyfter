import PySimpleGUI as sg
from datetime import datetime

def permanent_manager_window(manager):
    sg.theme('Light Blue 1')
    
    #Frame que contiene la tabla de movimientos, filtros por fecha y por tipo (Gasto o Ingreso)
    frame_layout1 = [
                    line_01_for_frame_01(manager),
                    line_02_for_frame_01(),
                    line_03_for_frame_01()
                    ]
    
    #Frame que muestra la leyenda de categorías y el filtro de las mismas
    frame_layout2 = [[[sg.Checkbox(cat.name, default=True, key=f'-CAT-{cat.name.upper()}-', checkbox_color=cat.color, enable_events=True)] for cat in manager.categories]]

    #Frame que contiene una botonera para agregar nuevos movimientos o categorías
    frame_layout3 = [[sg.Button('Agregar ingreso', key='-INCOME-'),sg.Button('Agregar gasto', key='-EXPENSE-'),sg.Button('Crear Categoría', key='-CATEGORY-')]]

    #Creación de los frames y montaje del layout completo
    layout = [[sg.Frame('Movimientos', frame_layout1), 
                sg.Frame('Categorías', frame_layout2, vertical_alignment='t', expand_y=True, key='-CATS-')],
                [sg.Frame('Gestionar', frame_layout3, expand_x=True)]]

    window = sg.Window('Gestor de Finanzas Personales', layout, finalize=True)
    return window 

def line_01_for_frame_01(manager):
    #*Filtro por fechas
    line_of_elements = [
        sg.Text('Fecha inicio:'),                                                                       #*Elemento 01 de la línea: -texto-
        sg.Input(manager.minor_date, size=10, enable_events=True, disabled= True, key='-START-'),       #*Elemento 02 de la línea: -casilla con la fecha menor para filtrar-
        sg.CalendarButton('Calendario', target='-START-', format="%d/%m/%Y"),                           #*Elemento 03 de la línea: -botón calendario para cambiar filtro-
        sg.Text('Fecha final:'),                                                                        #*Elemento 04 de la línea: -texto-
        sg.Input(manager.major_date, size=10, enable_events=True, disabled= True, key='-END-'),         #*Elemento 05 de la línea: -casilla con la fecha menor para filtrar-
        sg.CalendarButton('Calendario', target='-END-', format="%d/%m/%Y")                              #*Elemento 06 de la línea: -botón calendatio para cambiar filtro-
        ]
    return line_of_elements

def line_02_for_frame_01():
    #*Visualización de la tabla. Una única línea, un único elemento
    headers = ["Fecha","Tipo","Categoría","Título","Monto"]  
    line_of_elements = [
        sg.Table(
        values=[], headings=headers, expand_x=True, justification="left",
        auto_size_columns=False, col_widths=[8,7,12,18,9], key='-TABLE-', text_color="#400000"
        )
        ]
    return line_of_elements

def line_03_for_frame_01():
    #*Filtro por ingresos, gastos. Totales de ingresos, gastos, balance
    line_of_elements = [
        sg.Checkbox('Ingresos:', default=True, enable_events=True, key='-CHECK-INCOMES-'),       #*Elemento 1 de la línea: Checkbox para Ingresos
        sg.Multiline(0,s=10, no_scrollbar=True, key='-TOT-INCOMES-'),                            #*Elemento 2 de la línea: Output de los Ingresos Totales
        sg.Checkbox('Gastos:', default=True, enable_events=True, key='-CHECK-EXPENSES-'),        #*Elemento 3 de la línea: Checkbox para Gastos
        sg.Multiline(0,s=10, no_scrollbar=True, key='-TOT-EXPENSES-'),                           #*Elemento 4 de la línea: Output de los Gastos Totales
        sg.Text('Balance:'),                                                                     #*Elemento 5 de la línea: Texto
        sg.Multiline(0,s=10, no_scrollbar=True, key='-BALANCE-'),                                #*Elemento 6 de la línea: Output del Balance
        ]
    return line_of_elements

def add_movement_window(manager,type):
    date = datetime.now().strftime("%d/%m/%Y")
    translator = {'-INCOME-':'Ingreso','-EXPENSE-':'Gasto'}
    layout = [
            [sg.Text('Tipo', size=(8)), sg.Multiline(translator[type], s=8, no_scrollbar=True, key='-TYPE-', disabled=True)],
            [sg.Text('Fecha', size=(8)), sg.Input(size=12, default_text=date, key='-DATE-'), sg.CalendarButton('Calendario', target='-DATE-', format="%d/%m/%Y")],
            [sg.Text('Categoría', size=(8)), sg.Combo(values=[[cat.name][0] for cat in manager.categories], key='-CATEGORY-')],
            [sg.Text('Título', size=(8)), sg.InputText(key='-TITLE-')],
            [sg.Text('Monto', size=(8)), sg.Input(key='-AMOUNT-')],
            [sg.Text('', text_color='red', key='-ERROR-')],
            [sg.Button('Agregar'), sg.Button('Cancelar')]]
    window = sg.Window(f'Agregar {translator[type]}', layout)
    return window

def create_category_window():
    layout = [[sg.Text('Categoría', size=(8)), sg.InputText(key='-NAME-')],                     #*Línea 01
                [sg.ColorChooserButton('Elegir un color', target='-COLOR-'),                    #*Elemento 01 de la línea 02
                    sg.Text("", size=(2), background_color='white', key='-SAMPLE-'),            #*Elemento 02 de la línea 02
                    sg.Input(enable_events=True, size=5, visible=False, key='-COLOR-')],        #*Elemento 03 de la línea 02
                [sg.Text('', text_color='red', key='-ERROR-')],                                 #*Línea 03
                [sg.Button('Crear'), sg.Button('Cancelar')]]                                    #*Línea 04
    window = sg.Window(f'Crear Categoría', layout)
    return window
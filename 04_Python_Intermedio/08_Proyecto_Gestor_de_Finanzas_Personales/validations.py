from datetime import datetime

def validate_add_category(manager,values,window):
    if not values['-NAME-']:
        window['-NAME-'].update(background_color='pink')
        window['-ERROR-'].update("Debe digitar un nombre para la categoría")
        return False
    for cat in manager.categories:
        if cat.name.lower() == values['-NAME-'].lower():
            window['-NAME-'].update(background_color='pink')
            window['-ERROR-'].update("La categoría digitada ya existe")
            return False
    return True


def validate_add_movement(manager,values,window):  
    if validate_not_blanks(window,values):
        if validate_date(values,window):
            if validate_category_exists(manager,values,window):
                if validate_amount(values,window):
                    return True
    return False

def validate_not_blanks(window,values):
    translator = {'-DATE-':'fecha','-CATEGORY-':'categoría','-TITLE-':'título','-AMOUNT-':'monto'}
    empty_parameters = []
    for key in ['-DATE-','-CATEGORY-','-TITLE-','-AMOUNT-']:
        if not values[key]:
            empty_parameters.append(translator[key])
            window[key].update(background_color='pink')
        else:
            window[key].update(background_color='white')
    if len(empty_parameters) > 0:
        window['-ERROR-'].update(f'Error: Debe completar la información de {', '.join(empty_parameters)}')
        return False
    else:
        window['-ERROR-'].update("")
            
    return True

def validate_category_exists(manager,values,window):
    for cat in manager.categories:
        if cat.name.lower() == values['-CATEGORY-'].lower():
            window['-CATEGORY-'].update(background_color='white')
            return True
    window['-ERROR-'].update('Error: Debe ingresar únicamente una de las categorías disponibles')
    window['-CATEGORY-'].update(background_color='pink')
    return False

def validate_date(values,window):
    try:
        today = datetime.today()
        input_date = datetime.strptime(values['-DATE-'], "%d/%m/%Y")
        if input_date > today:
            window['-DATE-'].update(background_color='pink')
            window['-ERROR-'].update('Error: La fecha no puede ser posterior al día de hoy')
            return False
        window['-DATE-'].update(background_color='white')
        window['-ERROR-'].update('')
        return True
    except:
        window['-DATE-'].update(background_color='pink')
        window['-ERROR-'].update('Error: Debe digitar una fecha válida en el formato dd/mm/yyyy')
        return False

def validate_amount(values,window):
    try:
        amount = float(values['-AMOUNT-'])
        if (values['-TYPE-'] == "Ingreso") and (amount < 0):
            window['-AMOUNT-'].update(background_color='pink')  
            window['-ERROR-'].update('Error: el monto de un ingreso no puede ser negativo')
            return False
        window['-AMOUNT-'].update(background_color='white')
        window['-ERROR-'].update('')
        return True
    except:
        window['-AMOUNT-'].update(background_color='pink')
        window['-ERROR-'].update('Error: Debe digitar una cantidad válida en la casilla de monto')
        return False
    

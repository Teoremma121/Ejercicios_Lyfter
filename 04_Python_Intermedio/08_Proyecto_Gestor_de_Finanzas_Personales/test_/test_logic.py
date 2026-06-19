import classes as cl
import interface as ifc
import validations as vl
import layouts as ly
import PySimpleGUI as sg
from pathlib import Path
import os
import csv
from datetime import datetime, timedelta


def test_init_Finance_Manager():
    file_1 = Path("movements.csv")
    backup_1 = Path("movements.csv.bak")
    if file_1.exists():
        file_1.rename(backup_1)
    file_2 = Path("categories.csv")
    backup_2 = Path("categories.csv.bak")
    if file_2.exists():
        file_2.rename(backup_2)
    fm = cl.Finance_Manager()
    os.remove("movements.csv")
    if backup_1.exists():
        backup_1.rename(file_1)
    os.remove("categories.csv")
    if backup_2.exists():
        backup_2.rename(file_2)
    result = fm.movements
    assert result == []

def test_method_create_category_checking_from_object_attributes():
    file_1 = Path("movements.csv")
    backup_1 = Path("movements.csv.bak")
    if file_1.exists():
        file_1.rename(backup_1)
    file_2 = Path("categories.csv")
    backup_2 = Path("categories.csv.bak")
    if file_2.exists():
        file_2.rename(backup_2)
    fm = cl.Finance_Manager()
    fm.create_category('Trabajo','#8080c0')
    result = (fm.categories[0].name, fm.categories[0].color)
    os.remove("movements.csv")
    if backup_1.exists():
        backup_1.rename(file_1)
    os.remove("categories.csv")
    if backup_2.exists():
        backup_2.rename(file_2)
    assert result == ('Trabajo','#8080c0')

def test_method_create_movement_checking_from_object_attributes():
    file_1 = Path("movements.csv")
    backup_1 = Path("movements.csv.bak")
    if file_1.exists():
        file_1.rename(backup_1)
    file_2 = Path("categories.csv")
    backup_2 = Path("categories.csv.bak")
    if file_2.exists():
        file_2.rename(backup_2)
    fm = cl.Finance_Manager()
    fm.add_movement('25/04/2025','Gasto','Educación','Copias',5000)
    move = fm.movements[0]
    result = [move.date, move.type, move.category, move.title, move.amount]
    os.remove("movements.csv")
    if backup_1.exists():
        backup_1.rename(file_1)
    os.remove("categories.csv")
    if backup_2.exists():
        backup_2.rename(file_2)
    assert result == ['25/04/2025','Gasto','Educación','Copias',-5000]

def test_add_movement_checking_from_csv():
    file_1 = Path("movements.csv")
    backup_1 = Path("movements.csv.bak")
    if file_1.exists():
        file_1.rename(backup_1)
    file_2 = Path("categories.csv")
    backup_2 = Path("categories.csv.bak")
    if file_2.exists():
        file_2.rename(backup_2)
    fm = cl.Finance_Manager()
    fm.add_movement('25/03/2025','Ingreso','Trabajo','Quincena',350000)
    fm.add_movement('27/03/2025','Gasto','Comida','Diario',-150000)
    result = file_1.read_text(encoding="utf-8")
    expected = (
        "date,type,category,title,amount\n"
        "25/03/2025,Ingreso,Trabajo,Quincena,350000.0\n"
        "27/03/2025,Gasto,Comida,Diario,-150000.0\n"
    )
    os.remove("movements.csv")
    if backup_1.exists():
        backup_1.rename(file_1)
    os.remove("categories.csv")
    if backup_2.exists():
        backup_2.rename(file_2)
    assert result == expected

def test_filter_by_date():
    file_1 = Path("movements.csv")
    backup_1 = Path("movements.csv.bak")
    if file_1.exists():
        file_1.rename(backup_1)
    file_2 = Path("categories.csv")
    backup_2 = Path("categories.csv.bak")
    if file_2.exists():
        file_2.rename(backup_2)
    fm = cl.Finance_Manager()
    fm.add_movement('25/03/2025','Ingreso','Trabajo','Quincena',350000)
    fm.add_movement('27/03/2025','Gasto','Comida','Diario',-150000)
    rows = ifc.update_movements(fm)
    filtered_rows = ifc.filter_by_date(rows,'26/03/2025','27/03/2025')
    os.remove("movements.csv")
    if backup_1.exists():
        backup_1.rename(file_1)
    os.remove("categories.csv")
    if backup_2.exists():
        backup_2.rename(file_2)
    result = filtered_rows[0]
    expected = ['27/03/2025','Gasto','Comida','Diario',-150000]
    assert result == expected

def test_getting_info_from_existing_file():
    file_1 = Path("movements.csv")
    backup_1 = Path("movements.csv.bak")
    if file_1.exists():
        file_1.rename(backup_1)
    file_2 = Path("categories.csv")
    backup_2 = Path("categories.csv.bak")
    if file_2.exists():
        file_2.rename(backup_2)
    with open("categories.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["name","color"])
        writer.writerow(["Educación", "#00ffff"])
        writer.writerow(["Salud", "#8080c0"])
    fm = cl.Finance_Manager()
    resultado = (fm.categories[0].name, fm.categories[1].name)
    os.remove("movements.csv")
    if backup_1.exists():
        backup_1.rename(file_1)
    os.remove("categories.csv")
    if backup_2.exists():
        backup_2.rename(file_2)
    assert resultado == ('Educación','Salud')

def test_validate_amount_with_string_input():
    fm = cl.Finance_Manager()
    window = ly.add_movement_window(fm,'-EXPENSE-')
    while True:
        event, values = window.read(timeout=1)
        if event in (sg.TIMEOUT_EVENT):
            values = {'-AMOUNT-':'quince mil','-TYPE-':'Gasto'}
            vl.validate_amount(values,window)
            result = window['-ERROR-'].get()
            break
    window.close()  
    assert result == 'Error: Debe digitar una cantidad válida en la casilla de monto'

def test_validate_amount_with_negative_income():
    fm = cl.Finance_Manager()
    window = ly.add_movement_window(fm,'-INCOME-')
    while True:
        event, values = window.read(timeout=1)
        if event in (sg.TIMEOUT_EVENT):
            values = {'-AMOUNT-':'-15000','-TYPE-':'Ingreso'}
            vl.validate_amount(values,window)
            result = window['-ERROR-'].get()
            break
    window.close()  
    assert result == 'Error: el monto de un ingreso no puede ser negativo'

def test_validate_category_exists_False():
    file_1 = Path("movements.csv")
    backup_1 = Path("movements.csv.bak")
    if file_1.exists():
        file_1.rename(backup_1)
    file_2 = Path("categories.csv")
    backup_2 = Path("categories.csv.bak")
    if file_2.exists():
        file_2.rename(backup_2)
    fm = cl.Finance_Manager()
    fm.create_category('Trabajo','#8080c0')
    fm.create_category('Salud','#00ffff')
    window = ly.add_movement_window(fm,'-EXPENSE-')
    while True:
        event, values = window.read(timeout=1)
        if event in (sg.TIMEOUT_EVENT):
            values = {'-CATEGORY-':'Seguro'}
            vl.validate_category_exists(fm,values,window)
            result = window['-ERROR-'].get()
            break
    window.close()
    os.remove("movements.csv")
    if backup_1.exists():
        backup_1.rename(file_1)
    os.remove("categories.csv")
    if backup_2.exists():
        backup_2.rename(file_2)  
    assert result == 'Error: Debe ingresar únicamente una de las categorías disponibles'

def test_validate_category_exists_True():
    file_1 = Path("movements.csv")
    backup_1 = Path("movements.csv.bak")
    if file_1.exists():
        file_1.rename(backup_1)
    file_2 = Path("categories.csv")
    backup_2 = Path("categories.csv.bak")
    if file_2.exists():
        file_2.rename(backup_2)
    fm = cl.Finance_Manager()
    fm.create_category('Trabajo','#8080c0')
    fm.create_category('Salud','#00ffff')
    window = ly.add_movement_window(fm,'-EXPENSE-')
    while True:
        event, values = window.read(timeout=1)
        if event in (sg.TIMEOUT_EVENT):
            values = {'-CATEGORY-':'Salud'}
            result = vl.validate_category_exists(fm,values,window)
            break
    window.close()
    os.remove("movements.csv")
    if backup_1.exists():
        backup_1.rename(file_1)
    os.remove("categories.csv")
    if backup_2.exists():
        backup_2.rename(file_2)  
    assert result == True

def test_validate_date_after_today():
    wrong_date =  datetime.now() + timedelta(days=1)
    wrong_date = wrong_date.strftime("%d/%m/%Y")
    fm = cl.Finance_Manager()
    window = ly.add_movement_window(fm,'-EXPENSE-')
    while True:
        event, values = window.read(timeout=1)
        if event in (sg.TIMEOUT_EVENT):
            values = {'-DATE-':wrong_date}
            vl.validate_date(values,window)
            result = window['-ERROR-'].get()
            break
    window.close()
    assert result == 'Error: La fecha no puede ser posterior al día de hoy'

def test_validate_date_wrong_format():
    fm = cl.Finance_Manager()
    window = ly.add_movement_window(fm,'-EXPENSE-')
    while True:
        event, values = window.read(timeout=1)
        if event in (sg.TIMEOUT_EVENT):
            values = {'-DATE-':'2026-05-06'}
            vl.validate_date(values,window)
            result = window['-ERROR-'].get()
            break
    window.close()
    assert result == 'Error: Debe digitar una fecha válida en el formato dd/mm/yyyy'

def test_validate_date_True():
    date =  datetime.now() - timedelta(days=1)
    date = date.strftime("%d/%m/%Y")
    fm = cl.Finance_Manager()
    window = ly.add_movement_window(fm,'-EXPENSE-')
    while True:
        event, values = window.read(timeout=1)
        if event in (sg.TIMEOUT_EVENT):
            values = {'-DATE-':date}
            result = vl.validate_date(values,window)
            break
    window.close()
    assert result == True

def test_validate_not_blanks_with_some_blanks():
    fm = cl.Finance_Manager()
    window = ly.add_movement_window(fm,'-EXPENSE-')
    while True:
        event, values = window.read(timeout=1)
        if event in (sg.TIMEOUT_EVENT):
            values = {'-DATE-':'27/05/2026','-CATEGORY-':'','-TITLE-':'Suscripción Netflix','-AMOUNT-':''}
            vl.validate_not_blanks(window,values)
            result = window['-ERROR-'].get()
            break
    window.close()
    assert result == 'Error: Debe completar la información de categoría, monto'

def test_validate_not_blanks_True():
    fm = cl.Finance_Manager()
    window = ly.add_movement_window(fm,'-EXPENSE-')
    while True:
        event, values = window.read(timeout=1)
        if event in (sg.TIMEOUT_EVENT):
            values = {'-DATE-':'27/05/2026','-CATEGORY-':'Entretenimiento','-TITLE-':'Suscripción Netflix','-AMOUNT-':'-5000'}
            result = vl.validate_not_blanks(window,values)
            break
    window.close()
    assert result == True

def test_validate_add_category_empty():
    fm = cl.Finance_Manager()
    window = ly.create_category_window()
    while True:
        event, values = window.read(timeout=1)
        if event in (sg.TIMEOUT_EVENT):
            values = {'-NAME-':''}
            vl.validate_add_category(fm,values,window)
            result = window['-ERROR-'].get()
            break
    window.close()
    assert result == 'Error: Debe digitar un nombre para la categoría'

def test_validate_add_category_with_repeated_category():
    file_1 = Path("movements.csv")
    backup_1 = Path("movements.csv.bak")
    if file_1.exists():
        file_1.rename(backup_1)
    file_2 = Path("categories.csv")
    backup_2 = Path("categories.csv.bak")
    if file_2.exists():
        file_2.rename(backup_2)
    fm = cl.Finance_Manager()
    fm.create_category('Salud','#00ffff')
    window = ly.create_category_window()
    while True:
        event, values = window.read(timeout=1)
        if event in (sg.TIMEOUT_EVENT):
            values = {'-NAME-':'Salud'}
            vl.validate_add_category(fm,values,window)
            result = window['-ERROR-'].get()
            break
    window.close()
    os.remove("movements.csv")
    if backup_1.exists():
        backup_1.rename(file_1)
    os.remove("categories.csv")
    if backup_2.exists():
        backup_2.rename(file_2)  
    assert result == 'Error: Ya existe una categoría con el mismo nombre digitado'

def test_add_movement_event_successful():
    date =  datetime.now() - timedelta(days=1)
    date = date.strftime("%d/%m/%Y")
    file_1 = Path("movements.csv")
    backup_1 = Path("movements.csv.bak")
    if file_1.exists():
        file_1.rename(backup_1)
    file_2 = Path("categories.csv")
    backup_2 = Path("categories.csv.bak")
    if file_2.exists():
        file_2.rename(backup_2)
    fm = cl.Finance_Manager()
    fm.create_category('Entretenimiento','#00ffff')
    main_window = ly.permanent_manager_window(fm)
    sub_window = ly.add_movement_window(fm,'-EXPENSE-')
    while True:
        event, values = main_window.read(timeout=1)
        if event in (sg.TIMEOUT_EVENT):
            while True:
                event, values = sub_window.read(timeout=1)
                if event in (sg.TIMEOUT_EVENT):
                    values = {'-DATE-':date,'-TYPE-':'Gasto','-CATEGORY-':'Entretenimiento','-TITLE-':'Suscripción Netflix','-AMOUNT-':'5000'}
                    ifc.add_movement_event(fm,values,main_window,sub_window)
                    result = []
                    for attribute in ['date','type','category','title','amount']:
                        result.append(getattr(fm.movements[0],attribute))
                    break
            break
    sub_window.close()
    main_window.close()
    os.remove("movements.csv")
    if backup_1.exists():
        backup_1.rename(file_1)
    os.remove("categories.csv")
    if backup_2.exists():
        backup_2.rename(file_2)  
    assert result == [date,'Gasto','Entretenimiento','Suscripción Netflix',-5000]

def test_add_movement_event_category_fail():
    date =  datetime.now() - timedelta(days=1)
    date = date.strftime("%d/%m/%Y")
    fm = cl.Finance_Manager()
    storaged_movements = len(fm.movements)
    main_window = ly.permanent_manager_window(fm)
    sub_window = ly.add_movement_window(fm,'-EXPENSE-')
    while True:
        event, values = main_window.read(timeout=1)
        if event in (sg.TIMEOUT_EVENT):
            while True:
                event, values = sub_window.read(timeout=1)
                if event in (sg.TIMEOUT_EVENT):
                    values = {'-DATE-':date,'-TYPE-':'Gasto','-CATEGORY-':'Hobbies','-TITLE-':'Suscripción Netflix','-AMOUNT-':'5000'}
                    ifc.add_movement_event(fm,values,main_window,sub_window)
                    result = len(fm.movements)
                    break
            break
    sub_window.close()
    main_window.close()
    assert result == storaged_movements

def test_add_category_event_successful():
    date =  datetime.now() - timedelta(days=1)
    date = date.strftime("%d/%m/%Y")
    file_1 = Path("movements.csv")
    backup_1 = Path("movements.csv.bak")
    if file_1.exists():
        file_1.rename(backup_1)
    file_2 = Path("categories.csv")
    backup_2 = Path("categories.csv.bak")
    if file_2.exists():
        file_2.rename(backup_2)
    fm = cl.Finance_Manager()
    main_window = ly.permanent_manager_window(fm)
    sub_window = ly.add_movement_window(fm,'-EXPENSE-')
    while True:
        event, values = main_window.read(timeout=1)
        if event in (sg.TIMEOUT_EVENT):
            while True:
                event, values = sub_window.read(timeout=1)
                if event in (sg.TIMEOUT_EVENT):
                    values = {'-NAME-':'Entretenimiento','-COLOR-':'#00ffff'}
                    ifc.add_category_event(fm,values,main_window,sub_window)
                    result = []
                    result.append(fm.categories[0].name)
                    result.append(fm.categories[0].color)
                    break
            break
    sub_window.close()
    main_window.close()
    os.remove("movements.csv")
    if backup_1.exists():
        backup_1.rename(file_1)
    os.remove("categories.csv")
    if backup_2.exists():
        backup_2.rename(file_2)  
    assert result == ['Entretenimiento','#00ffff']

    